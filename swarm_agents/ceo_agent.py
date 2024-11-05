from swarm import Agent
from code_reviewer_agent import CodeReviewerAgent
from code_debugger_agent import CodeDebuggerAgent
from web_search_agent import WebSearchAgent
from solana_smart_contract_agent import SolanaSmartContractAgent
from vscode_coding_agent import VSCodeCodingAgent

class CEOAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CEO Agent",
            model="gpt-4o",
            instructions="Interpret tasks and assign to the appropriate agents.",
            functions=[self.delegate_task]
        )

    def delegate_task(self, context_variables):
        task = context_variables.get("task_description", "").lower()
        if "review" in task:
            return CodeReviewerAgent()
        elif "debug" in task:
            return CodeDebuggerAgent()
        elif "web search" in task:
            return WebSearchAgent()
        elif "solana" in task:
            return SolanaSmartContractAgent()
        elif "vscode" in task:
            return VSCodeCodingAgent()
        return "Task not understood. Please clarify."
