import os
from typing import Annotated
import asyncio
from openai import AsyncOpenAI, base_url
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.functions import kernel_function

import random


class DestinaltionsPlugin:
    """A List of Random Destinations for a vacation."""

    def __init__(self):
        self.destinations = [
            "Barcelona, Spain",
            "Paris, France",
            "Berlin, Germany",
            "Tokyo, Japan",
            "Sydney, Australia",
            "New York, USA",
            "Cairo, Egypt",
            "Cape Town, South Africa",
            "Rio de Janeiro, Brazil",
            "Bali, Indonesia"
        ]
        self.last_destination = None

    @kernel_function(description="Provides a random vacation destination.")
    def get_random_destination(self) -> Annotated[str, "Returns a random vacation destination."]:
        available_destinations = self.destinations.copy()
        if self.last_destination and len(available_destinations) > 1:
            available_destinations.remove()

        destination = random.choice(available_destinations)

        self.last_destination = destination

        return destination


load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://models.inference.ai.azure.com/",
)

chat_completion_service = OpenAIChatCompletion(
    ai_model_id="gpt-4o-mini",
    async_client=client,
)

agent = ChatCompletionAgent(
    service=chat_completion_service,
    plugins=[DestinaltionsPlugin()],
    name="TravelAgent",
    instructions="You are a helpful AI Agent that can help plan vacations for customers at random destinations",
)


async def main():
    thread: ChatHistoryAgentThread | None = None

    user_inputs = [
        "Plan me a day trip.",
    ]

    for user_input in user_inputs:
        print(f"# User:{user_input}\n")
        async for response in agent.invoke_stream(
                messages=user_input,
                thread=thread
        ):
            if first_chunk:
                print(f"#{response.name}:", end="", flush=True)
                first_chunk = False
            print(f"{response}", end="", flush=True)
            thread = response.thread
        print()

    await thread.delete() if thread else None


if __name__ == "__main__":
    asyncio.run(main())
