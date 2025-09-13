import re
from langsmith import traceable  
def extract_numbers(text):
    return [float(num) for num in re.findall(r"[-+]?\d*\.\d+|\d+", text)]

def sum_numbers(text):
    numbers = extract_numbers(text)
    if not numbers:
        return "No valid numbers found in the input."

    total = sum(numbers)
    numbers_str = " + ".join(map(str, numbers))
    return f"The sum of {numbers_str} is {total}."

@traceable(name="Handle agentic task")
def handle_agentic_task(intent, text):
    numbers = extract_numbers(text)
    if len(numbers) < 2:
        return "Please provide at least two numbers."

    a, b = numbers[0], numbers[1]

    if intent == 'add':
        return sum_numbers(text)
    elif intent == 'subtract':
        return f"The difference between {a} and {b} is {a - b}."
    elif intent == 'multiply':
        return f"The product of {a} and {b} is {a * b}."
    elif intent == 'divide':
        return f"The quotient of {a} divided by {b} is {a / b if b != 0 else 'undefined (division by zero)'}."
    else:
        return "Unknown task."
