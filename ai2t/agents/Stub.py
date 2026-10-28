from typing import Dict

from ai2t.agents.base import BaseAgent
from ai2t.working_memory.representation import Sai


class Stub(BaseAgent):
    """
    Just a dummy agent that requests no actions, doesn't learn, and returns
    false for all checks. Made for testing the API.
    """
    def request(self, state: Dict, **kwargs) -> Dict:
        return {}

    def train(self, state: Dict, sai: Sai, reward: float, **kwargs):
        pass

    def check(self, state: Dict, sai: Sai, **kwargs) -> float:
        return 0
