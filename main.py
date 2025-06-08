"""Run a simple 7-day simulation for the XAG agent."""

import openai
from memory import Memory
from world import World
from agent import Agent


def main():
    # Insert your API key here
    openai.api_key = "YOUR_API_KEY"

    memory = Memory()
    world = World()
    agent = Agent(memory, world, goal="Increase sales while keeping customers happy.")

    for _ in range(7):
        observation = world.observe()
        memory.remember(f"Observed: {observation}")

        action = agent.decide()
        result = world.apply(action)
        memory.remember(f"Action: {action}; Result: {result}")

        world.tick()
        print(f"Day {world.day} summary:")
        print(memory.recall(2))
        print("-")

    print("Final memory summary:")
    print(memory.summarize())


if __name__ == "__main__":
    main()
