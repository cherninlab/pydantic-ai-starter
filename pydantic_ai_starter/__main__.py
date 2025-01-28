import asyncio

import logfire

from pydantic_ai import Agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire="if-token-present")

# Example: If you set ANTHROPIC_API_KEY, or any other provider’s API key
# it’s automatically picked up by the relevant model if you're using them.

# Minimal agent w/ no tools, just a system prompt:
agent = Agent("claude-3-5-haiku-latest", system_prompt="You are a friendly assistant.")


async def main():
    print("Welcome to pydantic-ai-starter!")
    # A quick test run:
    answer = await agent.run("Say hello to CherninLab.")
    print("\nAgent answer:")
    print(answer.data)


if __name__ == "__main__":
    asyncio.run(main())
