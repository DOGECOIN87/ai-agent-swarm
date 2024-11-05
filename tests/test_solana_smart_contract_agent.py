import unittest
from swarm_agents.solana_smart_contract_agent import SolanaSmartContractAgent

class TestSolanaSmartContractAgent(unittest.TestCase):
    def test_handle_contract(self):
        agent = SolanaSmartContractAgent()
        result = agent.handle_contract("Sample Contract")
        self.assertIn("Processed Solana contract details", result)

if __name__ == "__main__":
    unittest.main()
