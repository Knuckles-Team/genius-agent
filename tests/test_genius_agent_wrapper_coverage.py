import genius_agent.agent_server
from unittest.mock import MagicMock, patch


def test_genius_agent_server_coverage():
    with (
        patch("agent_utilities.initialize_workspace"),
        patch("agent_utilities.load_identity", return_value={"name": "test"}),
        patch("agent_utilities.create_agent_server"),
        patch("agent_utilities.create_agent_parser") as mock_parser,
        patch("agent_utilities.build_system_prompt_from_workspace", return_value=""),
    ):
        mock_args = MagicMock()
        mock_args.debug = True
        mock_args.mcp_url = None
        mock_args.mcp_config = "mcp_config.json"
        mock_args.host = "localhost"
        mock_args.port = 8000
        mock_args.provider = "openai"
        mock_args.model_id = "gpt-4"
        mock_args.base_url = None
        mock_args.api_key = "test"
        mock_args.custom_skills_directory = None
        mock_args.web = False
        mock_args.otel = False
        mock_args.otel_endpoint = None
        mock_args.otel_headers = None
        mock_args.otel_public_key = None
        mock_args.otel_secret_key = None
        mock_args.otel_protocol = "http/protobuf"
        mock_args.evolve = False
        mock_parser.return_value.parse_args.return_value = mock_args

        from genius_agent.agent_server import agent_server

        agent_server()
