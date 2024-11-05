import unittest
from swarm_agents.web_search_agent import WebSearchAgent

class TestWebSearchAgent(unittest.TestCase):
    def test_search_web(self):
        agent = WebSearchAgent()
        result = agent.search_web("OpenAI")
        self.assertIn("Search results for 'OpenAI'", result)

if __name__ == "__main__":
    unittest.main()
