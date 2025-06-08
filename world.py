import random

class World:
    """A tiny business world simulation."""

    def __init__(self):
        self.day = 0
        self.sales = 0
        self.customers = 100
        self.feedback = []

    def observe(self) -> str:
        """Return a description of the current world state."""
        return (
            f"Day {self.day}, sales: {self.sales}, customers: {self.customers}, "
            f"feedback items: {len(self.feedback)}"
        )

    def apply(self, action: str) -> str:
        """Apply an action and update world state."""
        if action == "run_promo":
            delta = random.randint(10, 30)
            self.sales += delta
            self.feedback.append("Promo ran")
            return f"Ran promotion and gained {delta} sales"
        if action == "send_email":
            delta = random.randint(5, 15)
            self.sales += delta
            self.feedback.append("Email sent")
            return f"Sent marketing email and gained {delta} sales"
        return "Did nothing"

    def tick(self) -> None:
        """Advance the world one day."""
        self.day += 1
