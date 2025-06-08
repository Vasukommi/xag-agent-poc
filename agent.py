import openai

class Agent:
    """LLM-driven agent that selects an action based on memory and world state."""

    def __init__(self, memory, world, goal: str, model: str = "gpt-3.5-turbo-instruct"):
        self.memory = memory
        self.world = world
        self.goal = goal
        self.model = model

    def decide(self) -> str:
        """Ask the LLM for the next action."""
        prompt = (
            "You are an agent in a business simulation.\n"
            f"Goal: {self.goal}\n"
            f"World: {self.world.observe()}\n"
            f"Recent memory:\n{self.memory.recall(3)}\n"
            "Choose the next action from: run_promo, send_email, do_nothing.\n"
            "Respond with only the action."
        )
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        action = response.choices[0].message["content"].strip()
        if action not in {"run_promo", "send_email", "do_nothing"}:
            return "do_nothing"
        return action
