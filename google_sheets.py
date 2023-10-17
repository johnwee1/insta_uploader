# Retrieve message from google sheets or wherever it may get from
import gspread
import pandas as pd


def get_new_messages(filename: str = "sheets.json") -> tuple[list[str],list[str]]:
    """
    Retrieves new responses since the last time it run.
    :return: (list of names, list of messages) of new messages to process
    """

    gsa = gspread.service_account(filename=filename)
    sh = gsa.open("Test form spreadsheet")

    data = pd.DataFrame(sh.sheet1.get_all_records())
    # update sheet1 counter
    previous_number = data.loc[0,"PreviousNumber"]  # update counter
    print(f"previous_number = {previous_number}")
    print(f"data message size = {data.loc[:, 'Message'].size}")
    # assert previous_number == data.loc[:, "Message"].size
    name = data.loc[previous_number:, "Name"]
    message = data.loc[previous_number:, "Message"]
    assert len(name) == len(message)
    sh.sheet1.update(
        values=[[str(data.loc[0,"PreviousNumber"]+len(name))]],
        range_name="C2")
    return name.to_list(), message.to_list()


# name_list, message_list = get_new_messages()
# print(f"namelist: {name_list}")
# print(f"messagelist: {message_list}")

# gsa = gspread.service_account(filename='sheets.json')
# sh = gsa.open("Test form spreadsheet")
# # sh.sheet1.clear()
# data = pd.DataFrame(sh.sheet1.get_all_records())
# print(data)