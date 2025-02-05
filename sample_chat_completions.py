def sample_chat_completions():
    import os

    try:
        # endpoint = os.environ["AZURE_AI_CHAT_ENDPOINT"]
        # key = os.environ["AZURE_AI_CHAT_KEY"]
        endpoint = os.getenv("AZURE_AI_CHAT_ENDPOINT", "")
        key = os.getenv("AZURE_OPENAI_API_KEY", "")
    except KeyError:
        print("Missing environment variable 'AZURE_AI_CHAT_ENDPOINT' or 'AZURE_AI_CHAT_KEY'")
        print("Set them before running this sample.")
        exit()

    # [START chat_completions]
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential

    print("key:", key),
    print("endpoint:", endpoint)
    client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    print("client:", client)

    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant."),
            UserMessage("How many feet are in a mile?"),
        ]
    )

    print("结果为：")
    print(response.choices[0].message.content)
    # [END chat_completions]


if __name__ == "__main__":
    sample_chat_completions()
