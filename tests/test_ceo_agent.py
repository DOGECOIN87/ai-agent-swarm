import unittest
from swarm_agents.ceo_agent import CEOAgent

class TestCEOAgent(unittest.TestCase):
    def test_delegate_task(self):
        agent = CEOAgent()
        result = agent.delegate_task({"task_description": "review"})
        self.assertIn("Code Reviewer", result.name)

if __name__ == "__main__":
    unittest.main()
