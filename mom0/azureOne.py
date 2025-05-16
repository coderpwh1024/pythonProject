import os
from mem0 import Memory
from posthog import api_key

# azure_api_key=""
# azure_endpoint=""
# azure_modelId=""


azure_api_key = os.getenv("api_key","")
azure_endpoint = os.getenv("azure_endpoint","")
azure_modelId = os.getenv("azure_deployment"," ")

print("azure_api_key:", azure_api_key)
print("azure_endpoint:", azure_endpoint)
print("azure_modelId:", azure_modelId)

azureConfig = {
    "llm": {
        "provider": "azure_openai",
        "config": {
            "temperature": 0.1,
            "max_tokens": 8000,
            "azure_kwargs": {
                "azure_deployment": azure_modelId,
                "azure_endpoint": azure_endpoint,
                "api_key": azure_api_key,
                "api_version": "2024-05-01-preview"  # 必须设置
            }
        }
    }
}

m = Memory.from_config(azureConfig)

messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant",
     "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

response = m.generate("What is Azure OpenAI?")
print(response)
