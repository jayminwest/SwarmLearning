import os
import json
from colorama import init, Fore, Style

import openai
from groq import Groq
from swarm import Swarm, Agent
from swarm.repl import run_demo_loop

from agents import delegator
from utils.swarm_utils import pretty_print_messages, process_and_print_streaming_response

# Initialize colorama for cross-platform colored output
init()

def run_demo_loop_local(
    client, starting_agent, context_variables=None, stream=False, debug=False
) -> None:
    print("Starting Swarm CLI 🐝")

    messages = []
    agent = starting_agent

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

# LLM client setup
# llm = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="random")  # Local model
llm = openai.OpenAI()

# Swarm client setup
client = Swarm(client=llm)

# Main execution
if __name__ == "__main__":
    messages = []
    agent = delegator

    # Uncomment one of the following lines to run the desired loop
    # run_demo_loop_local(client=client, starting_agent=agent, stream=True)
    run_demo_loop(agent, stream=True)

"""
# Keeping the following code commented for future reference

context_variables = None
stream = None
debug = None

def print_welcome_message():
    print(f"{Fore.CYAN}Welcome to the Knowledge Management Swarm Chat!{Style.RESET_ALL}")
    print("You can interact with various agents to manage your Zettelkasten notes.")
    print("Type 'exit' to end the chat.")
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")

def print_separator():
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")

print_welcome_message()

while True:
    user_input = input(f"{Fore.GREEN}User: {Style.RESET_ALL}")
    
    if user_input.lower() == 'exit':
        print(f"{Fore.CYAN}Thank you for using the Knowledge Management Swarm Chat. Goodbye!{Style.RESET_ALL}")
        break
    
    messages.append({"role": "user", "content": user_input})

    response = client.run(
        agent=agent,
        messages=messages,
        context_variables=context_variables or {},
        stream=stream,
        debug=debug,
        max_turns=10
    )

    if stream:
        response = process_and_print_streaming_response(response)
    else:
        pretty_print_messages(response.messages)

    messages.extend(response.messages)
    agent = response.agent
    
    print_separator()
"""
