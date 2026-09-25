import os
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434/v1")

model = OllamaModel(
    "qwen3:1.7b",
    provider=OllamaProvider(base_url=OLLAMA_HOST),
)

agent = Agent(
    model,
    instructions=(
        "You are a helpful personal assistant running 100% locally. "
        "Use your tools whenever they can help answer the question. "
        "Keep your answers short and friendly."
    )
)

def main():
    print("Local agent ready! Type 'quit' or 'exit'.\n")
    history = []
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("quit", "exit"):
            break
        result = agent.run_sync(user_input, message_history=history)
        history = result.all_messages()
        print(result.output)

if __name__ == "__main__":
    main()