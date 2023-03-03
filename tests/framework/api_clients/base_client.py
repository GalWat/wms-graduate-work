import requests
from requests.exceptions import JSONDecodeError
from functools import wraps
import logging
import sys
from pprint import pformat

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def try_return_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("UPCOMING REQUEST")
        response = func(*args, **kwargs)

        logger.info(pformat({
            "request": {
                "url": response.request.url,
                "method": response.request.method,
                "body": response.request.body,
            },
            "response": {
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.text
            }
        }))

        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    return wrapper


class BaseClient:
    def __init__(self, service_url: str, local_run=False):
        self.service_url = f"http://{service_url.strip('/') if not local_run else '127.0.0.1:8080'}"

    @try_return_json
    def get(self, handler):
        return requests.get(f"{self.service_url}/{handler.strip('/')}")

    @try_return_json
    def post(self, handler, json):
        return requests.post(f"{self.service_url}/{handler.strip('/')}", json=json)
