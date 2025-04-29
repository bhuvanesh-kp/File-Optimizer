import os
import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def interact_with_llm(prompt: str) -> str:
    system_prompt = (
        "You are a helpful assistant that organizes and classifies system files. "
        "Use context to identify relevant files and suggest optimized storage locations."
    )
    full_prompt = f"<|start_header_id|>system<|end_header_id|>\n{system_prompt}\n<|start_header_id|>user<|end_header_id|>\n{prompt}\n<|start_header_id|>assistant<|end_header_id|>\n"

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "temperature": 0.3,
            "max_new_tokens": 512
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()[0]['generated_text']
        return result.split("<|end_header_id|>\n")[-1].strip()
    else:
        return f"API Error: {response.status_code} - {response.text}"


def identify_relevant_files(description, samples, all_files):
    # Simulated relevance: select files containing the word 'python' or description keyword
    keywords = [description.lower(), 'python']
    relevant = []

    for file in all_files:
        try:
            with open(file, 'r', errors="ignore") as f:
                content = f.read(512).lower()
                if any(k in content for k in keywords):
                    relevant.append(file)
        except:
            pass
    return relevant
