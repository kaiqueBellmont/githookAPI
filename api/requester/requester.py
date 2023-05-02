from dataclasses import dataclass
import requests
from .params import Params


@dataclass
class GitHookApiRequester:
    """
    A custom requester class.
    """

    request: requests = requests
    params: Params = Params()

    if not params:
        raise Exception("invalid or null params")

    def __str__(self) -> str:
        return f" request: {self.request}" f"Params: {self.params}"
