from swarm import Swarm
from ceo_agent import CEOAgent
from code_reviewer_agent import CodeReviewerAgent
from code_debugger_agent import CodeDebuggerAgent
from web_search_agent import WebSearchAgent
from solana_smart_contract_agent import SolanaSmartContractAgent
from vscode_coding_agent import VSCodeCodingAgent

def main():
    # Initialize agents
    ceo_agent = CEOAgent()
    code_reviewer = CodeReviewerAgent()
    code_debugger = CodeDebuggerAgent()
    web_searcher = WebSearchAgent()
    solana_agent = SolanaSmartContractAgent()
    vscode_agent = VSCodeCodingAgent()

    # Initialize Swarm client
    client = Swarm()

    # Set initial context and messages
    context_variables = {}
    messages = []

    # Start with the CEO agent
    agent = ceo_agent

    # Interaction loop
    while True:
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})

        # Run the Swarm client with current agent
        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables,
            debug=True,
        )

        # Print the response
        for message in response.messages:
            print(f"{message['sender']}: {message['content']}")

        # Update state for the next interaction
        messages.extend(response.messages)
        agent = response.agent

if __name__ == "__main__":
    main()
