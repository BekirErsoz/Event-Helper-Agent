
"""Eventify Helper Orchestrator"""
from .agents.greeting_agent import GreetingAgent
from .agents.event_search_agent import EventSearchAgent
from .agents.venue_recommender_agent import VenueRecommenderAgent
from .agents.weather_agent import WeatherAgent

class EventifyHelperAgent:
    def __init__(self):
        self.greeting = GreetingAgent()
        self.event_search = EventSearchAgent()
        self.venue = VenueRecommenderAgent()
        self.weather = WeatherAgent()

    def handle(self, message: str) -> str:
        text = message.lower()
        if any(w in text for w in ("hi", "hello", "selam", "merhaba")):
            return self.greeting.respond(message)
        if "weather" in text or "hava" in text:
            return self.weather.respond(message)
        if "event" in text or "etkinlik" in text:
            return self.event_search.respond(message)
        if "venue" in text or "mekan" in text:
            return self.venue.respond(message)
        return "Üzgünüm, şu an selamlama, etkinlik, mekân ve hava sorgularını yanıtlayabiliyorum."

def cli():
    import sys
    agent = EventifyHelperAgent()
    print(agent.handle(" ".join(sys.argv[1:])))

if __name__ == "__main__":
    cli()
