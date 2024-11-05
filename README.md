# AI Agent Swarm [For Coding Assistance]

This project is an AI agent framework that uses multiple specialized agents managed by a central CEO agent. Each agent has a unique responsibility, ranging from code review to debugging and web searching.

## Project Structure

- **swarm_controller.py**: Main controller file that manages all agents and coordinates task delegation.
- **swarm_agents/**: Contains each agent as a separate module.
- **tests/**: Contains test scripts for each agent.

## Setup Instructions

1. Clone the repository and navigate to the project root.
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
