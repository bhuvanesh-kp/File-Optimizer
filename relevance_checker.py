from llm_handler import interact_with_llm

def check_relevance(description, file_list):
    prompt = f"Given the description: '{description}', do these files match?\n\n"
    for path in file_list:
        try:
            with open(path, 'r', errors='ignore') as f:
                prompt += f"\n---\nFile: {path}\nContent:\n{f.read(300)}\n"
        except:
            prompt += f"\n---\nFile: {path}\n(Binary or unreadable file)"
    
    prompt += "\n\nRespond with 'yes' if relevant, 'no' otherwise."
    result = interact_with_llm(prompt).lower()
    return "yes" in result
