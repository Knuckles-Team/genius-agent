import unittest
from unittest.mock import patch
import os
import sys

# Add the project root to sys.path so we can import genius_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from genius_agent.genius_agent import create_agent


class TestSkillLoading(unittest.TestCase):
    @patch("genius_agent.genius_agent.SkillsToolset")
    @patch("genius_agent.genius_agent.get_skills_path")
    @patch("os.path.exists")
    def test_create_agent_with_custom_skills(
        self, mock_exists, mock_get_skills_path, mock_skills_toolset
    ):
        # Setup mocks
        mock_get_skills_path.return_value = "/default/skills"
        mock_exists.return_value = True

        # Call create_agent with custom skills directory
        create_agent(
            custom_skills_directory="/custom/skills", mcp_url="http://localhost:8080"
        )

        # Verify SkillsToolset was initialized with both directories
        # We expect one call to SkillsToolset with both directories
        # OR multiple calls if the implementation appends them separately.
        # Based on the plan: "Initialize SkillsToolset(directories=skill_dirs)" where skill_dirs has both.

        # Let's check how many times it was called and with what arguments.
        # The plan says:
        # skill_dirs = [get_skills_path()]
        # if custom_skills_directory: skill_dirs.append(custom_skills_directory)
        # skills = SkillsToolset(directories=skill_dirs)

        mock_skills_toolset.assert_called()
        call_args = mock_skills_toolset.call_args
        self.assertIsNotNone(call_args)

        # create_agent implementation detail check:
        # It might be called with directories argument
        kwargs = call_args.kwargs
        directories = kwargs.get("directories")

        self.assertIn("/default/skills", directories)
        self.assertIn("/custom/skills", directories)
        self.assertEqual(len(directories), 2)

    @patch("genius_agent.genius_agent.SkillsToolset")
    @patch("genius_agent.genius_agent.get_skills_path")
    @patch("os.path.exists")
    def test_create_agent_without_custom_skills(
        self, mock_exists, mock_get_skills_path, mock_skills_toolset
    ):
        # Setup mocks
        mock_get_skills_path.return_value = "/default/skills"
        mock_exists.return_value = True

        # Call create_agent WITHOUT custom skills directory
        create_agent(mcp_url="http://localhost:8080")

        mock_skills_toolset.assert_called()
        call_args = mock_skills_toolset.call_args
        kwargs = call_args.kwargs
        directories = kwargs.get("directories")

        self.assertIn("/default/skills", directories)
        self.assertEqual(len(directories), 1)


if __name__ == "__main__":
    unittest.main()
