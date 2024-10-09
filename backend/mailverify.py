# NOT FIXED, THIS WAS THE CODE IN THE LEGACY VERSION
import time

from simplegmail import Gmail
from simplegmail.query import construct_query
import re
from os import environ as env
import os
import dotenv
from time import sleep

dotenv.load_dotenv(".env")
assert "GMAIL_JSON" in env

csfile = "client_secret.json"


def retrieve_gmail_message() -> str:
    """
    With the configured OAuth credentials, retrieve the last message and return the 6 digit login code
    :return: str
    """
    time.sleep(10)
    with open(csfile, "w") as f:
        f.write(env["GMAIL_JSON"])  # Create a runtime instance of json file

    gmail = Gmail()

    os.remove(csfile)

    senders = ["security@mail.instagram.com", env["VERIFICATION_EMAIL"]]
    login_code = None
    messages = gmail.get_messages(
        query=construct_query(sender=senders, newer_than=(1, "day"))
    )
    print(messages)
    for message in messages:
        if message is None:
            break
        result = re.search(r"\b\d{6}\b", message.plain)
        if result is None:
            continue
        login_code = result.group()
        assert len(login_code) == 6
        message.trash()
        break

    print(f"mailverify.py: Login code = {login_code}")
    return login_code
