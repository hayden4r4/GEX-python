from tda.auth import easy_client
import atexit
from os.path import exists
from os import remove
import time
import json


# Set account variables and webdriver path
account_id: str = open("/mnt/z/API Keys/TD/TD_ACCOUNT_ID.txt").read()
consumer_key: str = open("/mnt/z/API Keys/TD/TD_CONSUMER_KEY.txt").read()
redirect_uri: str = "https://localhost"
token_path: str = "/mnt/z/API Keys/TD/ameritrade-credentials.json"
geckodriver_path: str = "/usr/local/bin/geckodriver"


def init(asyncio=False) -> easy_client:
    """
    Initializes api connection.
    Returns easy_client object.
    """

    def make_webdriver():
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        service: Service = Service(GeckoDriverManager().install())
        driver: webdriver.Firefox = webdriver.Firefox(service=service)
        atexit.register(lambda: driver.quit())
        return driver

    if exists(token_path):
        token = json.load(open(token_path))
        if token["token"]["expires_at"] < time.time():
            remove(token_path)

    c: easy_client = easy_client(
        consumer_key, redirect_uri, token_path, make_webdriver, asyncio
    )
    return c
