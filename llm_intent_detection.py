import subprocess
import re
import os
from langsmith import traceable  

@traceable(name="identify_intent_llm")
def identify_intent_llm(text):

    # Fallback rule-based override for command-style input
    if re.search(r'\b(run|execute|call|type)\b.*\b(command|dir|ls|whoami|mkdir|ping)\b', text, re.IGNORECASE):
        return "run_command"
    # Prompt to send to LLaMA3 for intent classification
    prompt = f"""
You are an intelligent assistant that detects user intent from natural language commands.
Classify the intent of the following message into one of these categories:
- add
- subtract
- multiply
- divide
- create_user
- delete_user
- list_users
- create_camera
- delete_camera
- list_camera
- run_command
- general

Examples:
- "Please add 2 and 3" -> add
- "Create a user named John" -> create_user
- "Run dir command" -> run_command
- "Execute command ls" -> run_command
- "Run windows command dir" -> run_command
- "List all cameras" -> list_camera

Now, respond with only the intent name, nothing else.

Respond with only the intent name, nothing else.

User input: "{text}"
Intent:
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        response = result.stdout.decode("utf-8").strip().lower()
        
        # Optionally sanitize unexpected responses
        valid_intents = {
            "add", "subtract", "multiply", "divide",
            "create_user", "delete_user", "list_users", "create_camera", "delete_camera", "list_camera", "run_command" "general"
        }

        for intent in valid_intents:
            if intent in response:
                return intent

        return "general"  # fallback if unknown

    except Exception as e:
        print(f"Error during intent detection: {e}")
        return "general"
