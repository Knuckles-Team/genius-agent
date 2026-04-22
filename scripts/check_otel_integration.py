#!/usr/bin/env python
import os
import base64
import logging
import logfire
from dotenv import load_dotenv
from pydantic_ai import Agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_otel():

    load_dotenv()

    print("--- OpenTelemetry Integration Check ---")

    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
    pk = os.getenv("OTEL_EXPORTER_OTLP_PUBLIC_KEY")
    sk = os.getenv("OTEL_EXPORTER_OTLP_SECRET_KEY")
    enable_otel = os.getenv("ENABLE_OTEL", "False").lower() == "true"

    print(f"ENABLE_OTEL: {enable_otel}")
    print(f"OTLP Endpoint: {endpoint}")
    print(f"Public Key: {pk[:10] if pk else ''}...{pk[-4:] if pk else ''}")
    print(f"Secret Key: {sk[:10] if sk else ''}...{sk[-4:] if sk else ''}")

    if not enable_otel:
        print("ERROR: ENABLE_OTEL is not set to True. OTel export will be disabled.")
        return

    if not endpoint:
        print("ERROR: OTEL_EXPORTER_OTLP_ENDPOINT is missing.")
        return

    if not os.getenv("OTEL_EXPORTER_OTLP_HEADERS") and pk and sk:
        auth_string = f"{pk}:{sk}"
        auth_encoded = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {auth_encoded}"
        print("Successfully generated OTLP Authorization headers.")
    else:
        print("Auth headers already set or keys missing.")

    print("\nInitializing Logfire...")
    try:
        logfire.configure(
            send_to_logfire=False,
            service_name="otel-validation-script",
            distributed_tracing=True,
        )
        logfire.instrument_pydantic_ai()
        print("Logfire configured and pydantic-ai instrumented.")
    except Exception as e:
        print(f"FAILED to configure Logfire: {e}")
        return

    print("\nSending test trace via pydantic-ai...")
    try:

        agent = Agent("openai:gpt-4o", system_prompt="You are a validator.")

        with logfire.span("Verification Span"):
            print("Trace span 'Verification Span' started...")
            logfire.info("Check: Connection to Langfuse is being attempted.")
            print("Simulating activity...")

        print("\nTrace sent successfully (locally).")
        print(
            "Please check your Langfuse dashboard to see if 'otel-validation-script' or 'Verification Span' appears."
        )
        print("Wait a few seconds for the exporter to flush the spans.")

    except Exception as e:
        print(f"FAILED to send trace: {e}")


if __name__ == "__main__":
    check_otel()
