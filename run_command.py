from langchain_core.tools import tool
import os
from langsmith import traceable  
import re

def extract_command(text):
    match = re.search(r"(?:run|execute|type|use|perform|call)\s+([a-zA-Z0-9_./\\-]+)", text, re.IGNORECASE)
    return match.group(1) if match else None

@traceable(name="handle command execution")
def run_command (intent, text):
    print('I am here: ', text)
    command = extract_command(text)
    print('Command : ', command)

    if command == 'ls':
        run_shell_command_safe('ls')
    elif command == 'dir':
        run_shell_command_safe('dir')
    elif command == 'whoami':
        run_shell_command_safe('whoami')
    else:
        return "Unsupported user operation."

# Tool to run shell commands
@tool
def run_shell_command(command: str) -> str:
    """Runs a shell command like dir or ls."""
    try:
        return os.popen(command).read()
    except Exception as e:
        return str(e)
    
def run_shell_command_safe2(command: str) -> str:
    allowed = ["dir", "ls"]
    if command.strip().split()[0] not in allowed:
        return "Command not allowed."
    return os.popen(command).read()

def run_shell_command_safe3(command: str) -> str:
    allowed = ["dir", "ls"]
    command_parts = command.strip().split()
    
    if not command_parts or command_parts[0] not in allowed:
        return "❌ Command not allowed. Only 'dir' or 'ls' are permitted."

    try:
        output = os.popen(command).read()
        if not output.strip():
            return "⚠️ Command executed, but no output was returned."
        return f"✅ **Command Output:**\n```\n{output.strip()}\n```"
    except Exception as e:
        return f"❌ Error while executing command: {str(e)}"
    
    import os

def run_shell_command_safe(command: str) -> str:
    # Include whoami to allow username lookup
    allowed = ["dir", "ls", "whoami"]
    command_parts = command.strip().split()

    if not command_parts or command_parts[0] not in allowed:
        return "❌ Command not allowed. Only 'dir', 'ls', or 'whoami' are permitted."

    try:
        # Execute the shell command
        output = os.popen(command).read().strip()

        # Handle empty output
        if not output:
            return "⚠️ Command executed, but no output was returned."

        # Custom message for whoami
        if command_parts[0] == "whoami":
            return f"👤 **Current User:** `{output}`"

        # Default formatted output
        return f"✅ **Command Output:**\n```\n{output}\n```"

    except Exception as e:
        return f"❌ Error while executing command: {str(e)}"

