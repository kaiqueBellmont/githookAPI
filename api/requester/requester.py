from dataclasses import dataclass
import requests
from .params import Params


@dataclass
class GitHookApiRequester:
    """
    #
    """
    request: requests = requests
    params: Params = Params()

    if not params:
        raise Exception("invalid or null params")

    def __str__(self):
        return f' request: {self.request}' \
               f'Params: {self.params}'




