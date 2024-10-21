from typing import List, Optional
from swarm import Agent

class Response:
    def __init__(self, agent: Optional[Agent], messages: list[dict]):
        self.agent = agent
        self.messages = messages
