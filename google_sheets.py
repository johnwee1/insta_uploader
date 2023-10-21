# Retrieve message from google sheets or wherever it may get from
import gspread
import pandas as pd
import json
from os import environ as env
import dotenv
dotenv.load_dotenv(".env")


def get_new_messages() -> tuple[list[str],list[str]]:
    """
    Retrieves new responses since the last time it run.
    :return: (list of names, list of messages) of new messages to process
    """
    creds_file = json.loads(env["SHEETS_JSON"])
    gsa = gspread.service_account_from_dict(creds_file)
    sh = gsa.open("Test form spreadsheet")

    data = pd.DataFrame(sh.get_worksheet(0).get_all_records())  # form data from Google sheets

    # Previous number tracks the index of the last message, since new message rows are inserted into bottom of list

    previous_sheets_row = sh.get_worksheet(1).acell("A1")  # $ == '1' means that previously, response sheet was empty
    previous_idx = int(previous_sheets_row.value) - 1  # offset by 1 such that the value refers to Pandas index.

    name = data.loc[previous_idx:, "Name"]
    message = data.loc[previous_idx:, "Message"]
    assert len(name) == len(message)
    idx = len(name) + previous_idx
    sheets_row = idx + 1  # Add back the offset to return to list
    print(f"{sheets_row}")

    sh.get_worksheet(1).update_acell('A1', sheets_row)
    return name.to_list(), message.to_list()

# names, messages =  get_new_messages()


