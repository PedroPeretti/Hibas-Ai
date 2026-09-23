import requests

MODEL = "qwen3:8b"
OLLAMA_URL = "http://localhost:11434/api/chat"

print("=" * 50)
print("              H I B A S   A I")
print("                    v0.1")
print("=" * 50)
print(f"Modelo: {MODEL}")
print("Digite /exit para sair.")
print()

messages = []

while True:
    user_input = input("Você > ")

    if user_input.lower() == "/exit":
        print("\nHIBAS > Até mais.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        }
    )

    data = response.json()

    answer = data["message"]["content"]

    print(f"\nHIBAS > {answer}\n")

    messages.append({
        "role": "assistant",
        "content": answer
    })