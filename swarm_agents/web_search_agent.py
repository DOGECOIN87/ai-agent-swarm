from swarm import Agent

class WebSearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Web Searcher",
            model="gpt-4o",
            instructions="Search the web for the requested information.",
            functions=[self.search_web]
        )

    def search_web(self, query: str) -> str:
        # Simulate a web search operation
        return f"Search results for '{query}' - [Result 1, Result 2]"
