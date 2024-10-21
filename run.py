from swarm import Swarm, Agent
from agents import delegator
import os, json
import openai
from utils.swarm_utils import pretty_print_messages, process_and_print_streaming_response


# Change the base url to the local llama3.2:3b model
llm = openai.OpenAI(base_url="http://localhost:11434/v1",api_key="random")

client = Swarm(client=llm)

messages = []
agent = delegator

context_variables = None
stream = None
debug = None

while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(
        agent=agent,
        messages=messages,
        context_variables=context_variables or {},
        stream=stream,
        debug=debug,
    )

    if stream:
        response = process_and_print_streaming_response(response)
    else:
        pretty_print_messages(response.messages)

    messages.extend(response.messages)
    agent = response.agent

