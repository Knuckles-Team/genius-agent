#!/usr/bin/env python
# coding: utf-8

import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

ossinsight_api_schema = {
    "name": "ossinsight_data_api",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": (
                    "Enter your GitHub data question in the form of a clear and specific question to ensure the returned data is accurate and valuable. "
                    "For optimal results, specify the desired format for the data table in your request."
                ),
            }
        },
        "required": [
            "question"
        ]
    },
    "description": "This is an API endpoint allowing users (analysts) to input question about GitHub in text format to retrieve the realted and structured data."
}


def exec_get_ossinsight(question):
    """
    Retrieve the top 10 developers with the most followers on GitHub.
    """
    url = "https://api.ossinsight.io/explorer/answer"
    headers = {"Content-Type": "application/json"}
    data = {
        "question": question,
        "ignoreCache": True
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        answer = response.json()
    else:
        return f"Request to {url} failed with status code: {response.status_code}"

    report_components = []
    report_components.append(f"Question: {answer['question']['title']}")
    if answer['query']['sql'] != "":
        report_components.append(f"querySQL: {answer['query']['sql']}")

    if answer.get('result', None) is None or len(answer['result']['rows']) == 0:
        result = "Result: N/A"
    else:
        result = "Result:\n  " + "\n  ".join([str(row) for row in answer['result']['rows']])
    report_components.append(result)

    if answer.get('error', None) is not None:
        report_components.append(f"Error: {answer['error']}")
    return "\n\n".join(report_components)
