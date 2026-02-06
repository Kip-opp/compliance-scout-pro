import os
from groq import Groq # We use the Groq library instead
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def audit_file(file_path):
    print(f"🔍 Auditing with Groq: {file_path}")
    
    with open(file_path, 'r', errors='ignore') as f:
        code_content = f.read()

    # The same security prompt
    prompt = f"You are an Elite Security Auditor. Analyze this code for bugs: {code_content}"

    # Call Groq's fast model
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    report = audit_file("scout.py")
    print("\n--- SECURITY REPORT ---")
    print(report)