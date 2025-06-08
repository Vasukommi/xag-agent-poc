import datetime

class Memory:
    """Simple memory to store events with timestamps and mood."""

    def __init__(self):
        self.log = []
        self.mood = "neutral"

    def remember(self, event: str) -> None:
        """Record an event with the current mood and timestamp."""
        self.log.append({
            "time": datetime.datetime.now(),
            "event": event,
            "mood": self.mood
        })

    def recall(self, n: int = 5) -> str:
        """Return the last n events as a formatted string."""
        entries = self.log[-n:]
        return "\n".join(
            f"{e['time'].isoformat()} - {e['event']} (mood: {e['mood']})"
            for e in entries
        )

    def set_mood(self, mood: str) -> None:
        """Update current mood."""
        self.mood = mood

    def summarize(self) -> str:
        """Summarize all events."""
        return "\n".join(
            f"{e['time'].strftime('%Y-%m-%d')}: {e['event']}"
            for e in self.log
        )
