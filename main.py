from ollama import chat

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an HR agent do in 1 short sentence."
        }
    ],
)


print(response.message.content)

