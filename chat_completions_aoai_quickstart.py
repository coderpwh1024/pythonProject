import os

from OpenAiFunction import client, endpoint

os.environ["AZURE_OPENAI_ENDPOINT"] =  os.getenv("AZURE_OPENAI_API_KEY", "")

endpoint = os.getenv("ENDPOINT_URL", "")
deployment = os.getenv("DEPLOYMENT_NAME", "")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")

def chat_completions_aoai_quickstart() -> None:
    #[START chat_completions_aoai_quickstart]
    import os
    from openai import AzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )



    client = AzureOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version=os.environ["API_VERSION_GA"],
    )

    response = client.chat.completions.create(
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Does Azure OpenAI support customer managed keys?",
            },
            {
                "role": "assistant",
                "content": "Yes, customer managed keys are supported by Azure OpenAI.",
            },
            {"role": "user", "content": "Do other Azure AI services support this too?"},
        ],
    )

    print(response.to_json())


if __name__=="__main__":
     chat_completions_aoai_quickstart()
