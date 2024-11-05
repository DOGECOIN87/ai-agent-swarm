import unittest
from swarm_agents.code_debugger_agent import CodeDebuggerAgent

class TestCodeDebuggerAgent(unittest.TestCase):
    def test_debug_code(self):
        agent = CodeDebuggerAgent()
        result = agent.debug_code("def foo(): pass")
        self.assertIn("No errors detected", result)

if __name__ == "__main__":
    unittest.main()
