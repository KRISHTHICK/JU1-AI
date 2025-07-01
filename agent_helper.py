import subprocess

def ask_finance_agent(prompt):
    query = f"A user asks about personal finance: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", query], capture_output=True, text=True)
    return result.stdout.strip()
