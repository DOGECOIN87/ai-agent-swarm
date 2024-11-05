
# AI Agent Swarm [For Coding Assistance]

This project is an AI agent framework that uses multiple specialized agents managed by a central CEO agent. Each agent has a unique responsibility, ranging from code review to debugging and web searching, all coordinated to streamline and enhance the coding workflow.

## Project Structure

- **`swarm_controller.py`**: Main controller that initializes and coordinates interactions among all agents.
- **`swarm_agents/`**: Contains each agent as a separate module, each specializing in a particular coding or development-related task.
- **`tests/`**: Contains test scripts for each agent to validate their functionalities.

## Setup Instructions

1. **Clone the Repository**: Clone this repository and navigate to the project root.
   ```bash
   git clone https://github.com/yourusername/ai-agent-swarm.git
   cd ai-agent-swarm
   ```

2. **Create a Virtual Environment** and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**: Install the required packages specified in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**: Create a `.env` file in the root directory with your API keys. For example:
   ```plaintext
   # .env file in the project root
   OPENAI_API_KEY=your_openai_api_key_here
   CLINE_API_KEY=your_cline_api_key_here
   ```

5. **Run the Application**: Start the application by running `swarm_controller.py`:
   ```bash
   python swarm_controller.py
   ```

## Agent Overview

### CEO Agent
- **Purpose**: Manages task delegation and interprets high-level instructions to assign tasks to other agents.
- **Example Task**: "Review code" - delegates to `CodeReviewerAgent`.

### Code Reviewer Agent
- **Purpose**: Reviews code for quality, improvements, and possible optimizations.
- **Example Task**: Receives code snippets and provides suggestions or highlights issues.

### Code Debugger Agent
- **Purpose**: Analyzes code snippets for errors and suggests fixes.
- **Example Task**: Identifies syntax and logical issues within given code snippets.

### Web Search Agent
- **Purpose**: Performs web searches to retrieve information as required by the CEO.
- **Example Task**: Conducts searches for programming-related questions or documentation.

### Solana Smart Contract Agent
- **Purpose**: Assists with Solana-based development tasks, focusing on smart contracts.
- **Example Task**: Interprets and validates smart contract details, performs basic checks, and assists with contract-related queries.

### VSCode Coding Agent
- **Purpose**: Interacts with VSCode to execute commands and edit files, using Cline's AI-assisted coding capabilities.
- **Example Task**: Modifies files, runs Cline commands, and integrates with VSCode for seamless coding workflows.

## Testing

To ensure each agent functions as expected, individual test files are included in the `tests/` directory. To run all tests:

```bash
python -m unittest discover tests
```

## Example Usage

1. **Run the Application**: Start by executing `swarm_controller.py`.
2. **Interact with Agents**: The CEO agent will handle your input, delegate tasks to the appropriate agents, and return consolidated results.
   - **Example Prompt**: Enter "Please review the code in `main.py`," and the CEO agent will delegate to the Code Reviewer Agent.
3. **Modify Files**: Use commands that interact with `VSCodeCodingAgent` to perform file modifications or run commands in VSCode.

## Configuration Options

### `.env` Configuration
The `.env` file holds sensitive keys and configuration settings. Add your API keys as follows:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
CLINE_API_KEY=your_cline_api_key_here
```

These keys allow agents to access OpenAI's API for model interactions and Cline's API for VSCode integration.
