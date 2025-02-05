import os
import base64
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "")
deployment = os.getenv("DEPLOYMENT_NAME", "")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")

# 使用基于密钥的身份验证来初始化 Azure OpenAI 客户端
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

assistant_1 = client.beta.assistants.create(
  name="Weather Bot",
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="LocalTest", #Replace with model deployment name
  tools=[{
      "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name, for example San Francisco"}
        },
        "required": ["location"]
      }
    }
  }]
)

# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

# 准备聊天提示
# chat_prompt = [
#     {
#         "role": "system",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "扮演一个机器人。"
#             }
#         ]
#     },
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "深圳的天气怎么样"
#             }
#         ]
#     }
# ]


# Create a thread
thread_1 = client.beta.threads.create()

# Add a user question to the thread
message_1 = client.beta.threads.messages.create(
    thread_id=thread_1.id,
    role="user",
    content="Is Shanghai raining now?"
)
message_2 = client.beta.threads.messages.create(
    thread_id=thread_1.id,
    role="assistant",
    content="No, it is not raining in Shanghai right now. It is 80°F and slightly cloudy."
)
message_3 = client.beta.threads.messages.create(
    thread_id=thread_1.id,
    role="user",
    content="What's the weather like?"
)
# Run the thread
run = client.beta.threads.runs.create(
  thread_id=thread_1.id,
  assistant_id=assistant_1.id,
)

import time
status = run.status
# Wait till the assistant has responded
while status not in ["completed", "cancelled", "expired", "failed","requires_action"]:
    time.sleep(5)
    run = client.beta.threads.runs.retrieve(thread_id=thread_1.id,run_id=run.id)
    status = run.status

print(run.status)
print(run.required_action)


# Example function
def get_weather():
    return "It's 80 degrees F and slightly cloudy."


# Define the list to store tool outputs
tool_outputs = []

# Loop through each tool in the required action section
for tool in run.required_action.submit_tool_outputs.tool_calls:
    # get data from the weather function
    if tool.function.name == "get_weather":
        print(tool.function.arguments)
        weather = get_weather()
        tool_outputs.append({
            "tool_call_id": tool.id,
            "output": weather
        })

# Submit all tool outputs at once after collecting them in a list
if tool_outputs:
    try:
        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread_1.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
        print("Tool outputs submitted successfully.")
    except Exception as e:
        print("Failed to submit tool outputs:", e)
else:
    print("No tool outputs to submit.")

status = run.status
# Wait till the assistant has responded
while status not in ["completed", "cancelled", "expired", "failed","requires_action"]:
    time.sleep(5)
    run = client.beta.threads.runs.retrieve(thread_id=thread_1.id,run_id=run.id)
    status = run.status

messages = client.beta.threads.messages.list(
  thread_id=thread_1.id
)

print(messages.model_dump_json(indent=2))