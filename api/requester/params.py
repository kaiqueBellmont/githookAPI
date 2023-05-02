"""
file responsible for the req parameters.
"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Params:
    """
    Params class
    """

    load_dotenv()  # take environment variables from .env.
    OPEN_AI_WORKER_ENDPOINT = os.getenv("WORKER_ENDPOINT")
    TEST_WORKER_ENDPOINT = os.getenv("TEST_WORKER_ENDPOINT")
    TEST_API_INTEGRATION_ENDPOINT = os.getenv("TEST_API_INTEGRATION_ENDPOINT")
