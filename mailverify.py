from simplegmail import Gmail
from simplegmail.query import construct_query
import re
from os import environ as env
import os
import dotenv

dotenv.load_dotenv('.env')
assert "GMAIL_JSON" in env

csfile = 'client_secret.json'


def retrieve_gmail_message():
    with open(csfile,'w') as f:
        f.write(env["GMAIL_JSON"])  # Create a runtime instance of json file

    gmail = Gmail()

    os.remove(csfile)

    senders = [
        "security@mail.instagram.com",
        "johnwee@outlook.com"  # for testing
    ]

    messages = gmail.get_messages(query=construct_query(sender=senders, newer_than=(1, 'day')))
    message = messages[0]

    login_code = re.search(r"\b\d{6}\b", message.plain).group()
    assert len(str(login_code)) == 6

    # If code is found, delete the message.
    message.trash()

    return login_code