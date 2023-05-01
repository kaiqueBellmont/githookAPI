import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Params:
    load_dotenv()  # take environment variables from .env.
    OPEN_AI_WORKER_ENDPOINT = os.getenv("WORKER_ENDPOINT")


