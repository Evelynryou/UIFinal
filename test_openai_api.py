import sys
import openai

openai.api_key = "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"  # your API key

if not openai.api_key:
    print("Please specify the OPENAI API KEY.", file=sys.stderr)
    sys.exit(1)

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="""
Fix grammar errors:
- I is a boy
- You is a girl""".strip(),
)

print(response)

print(response.choices[0].text.strip())

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a knowledgeable assistant."},
        {"role": "user", "content": "What is the largest city in the world?"}
    ],
)

print(response)
print(response["choices"][0]["message"]["content"])