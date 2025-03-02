import os
from mem0 import Memory

azure_api_key="",
azure_api_base="",
azure_api_version="2024-05-01-preview",
modelId="",

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": modelId,
            "OPENAI_API_KEY":azure_api_key,
            "AZURE_API_BASE":azure_api_base,
            "AZURE_API_VERSION":azure_api_version,
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})