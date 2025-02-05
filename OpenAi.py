import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "h")
deployment = os.getenv("DEPLOYMENT_NAME", "")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

response = client.chat.completions.create(
    model="Server",  # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "如何快速上手python"},
    ]
)

print("请求结果为:", response.choices[0].message.content)
