import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot that helps with learning English."},
        {"role": "user", "content": "Let's have a conversation."},
    ],
)

print(response)

# Print only the response message
print(response["choices"][0]["message"]["content"])