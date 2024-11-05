import unittest
from swarm_agents.code_reviewer_agent import CodeReviewerAgent

class TestCodeReviewerAgent(unittest.TestCase):
    def test_review_code(self):
        agent = CodeReviewerAgent()
        result = agent.review_code("def foo(): pass")
        self.assertIn("No issues found", result)

if __name__ == "__main__":
    unittest.main()
