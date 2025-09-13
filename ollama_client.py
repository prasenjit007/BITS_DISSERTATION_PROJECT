import requests

def query_ollama(prompt, model='llama3'):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Error communicating with the model."
