import requests
import json

API_URL = "https://api.openai.com/v1/completions"
API_KEY = "your_openai_api_key"  # add security for the key generation

def get_explanation(code_snippet):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4",
        "prompt": f"Explain this code: {code_snippet}",
        "max_tokens": 200
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        explanation = response.json()["choices"][0]["text"]
        return explanation
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    code_snippet = input("Enter a code snippet: ")
    explanation = get_explanation(code_snippet)
    print("Explanation:", explanation)
