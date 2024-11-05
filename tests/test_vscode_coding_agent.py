import unittest
from swarm_agents.vscode_coding_agent import VSCodeCodingAgent

class TestVSCodeCodingAgent(unittest.TestCase):
    def test_modify_file(self):
        agent = VSCodeCodingAgent()
        result = agent.modify_file("test_file.py", "print('Hello World')")
        self.assertIn("updated successfully", result)

if __name__ == "__main__":
    unittest.main()
