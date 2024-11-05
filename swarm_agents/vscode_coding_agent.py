from swarm import Agent
import subprocess

class VSCodeCodingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="VSCode Agent",
            model="gpt-4o",
            instructions="Use Cline in VSCode to perform coding tasks and modify files based on CEO instructions.",
            functions=[self.run_cline_command, self.modify_file]
        )

    def run_cline_command(self, command: str) -> str:
        """
        Executes a command in the VSCode terminal using Cline.
        Example usage: command = "cline generate --prompt 'Write a test for main.py'"
        """
        try:
            # Run the command in a subprocess, capturing the output
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return f"Command executed successfully:\n{result.stdout}"
            else:
                return f"Command failed with error:\n{result.stderr}"
        except Exception as e:
            return f"Error executing command '{command}': {str(e)}"

    def modify_file(self, file_path: str, content: str) -> str:
        """
        Directly writes content to a specified file within the VSCode workspace.
        This function allows the CEO agent to request file modifications.
        """
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return f"File '{file_path}' updated successfully."
        except Exception as e:
            return f"Error updating file '{file_path}': {str(e)}"
