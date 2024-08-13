# pylint: disable=import-error
from sheetsapi.get_env import get_env
from sheetsapi.google_auth.credentials import get_build

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_values():
    service = get_build()
    # pylint: disable=no-member
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=get_env()[0],
        range=get_env()[2],
        majorDimension="COLUMNS",
    ).execute()
    return result.get("values", [])


def find_column_index(values, event_name, name):
    for i, column in enumerate(values):
        if column[0] == event_name:
            if name in column:
                return -2, -2
            return i, len(column) + 1
    return -1, -1


def create_event_column(event_name):
    """
    Creates a new column for the event in the spreadsheet
    """
    # pylint: disable=no-member
    sheet = get_values().spreadsheets()
    body = {
        "values": [[event_name]]
    }
    sheet.values().append(
        spreadsheetId=get_env()[0],
        range=get_env()[2],
        valueInputOption="RAW",
        body=body
    ).execute()


def add_to_event(event_name, name):
    """
    Adds attendees name under event in the spreadsheet
    """
    # pylint: disable=no-member
    values = get_values()
    alpha_index, index = find_column_index(values, event_name, name)

    # if the name is already in the event, we don't need to do anything
    if alpha_index == -2:
        return

    if alpha_index == -1:
        create_event_column(event_name)

        values = get_values()
        alpha_index, index = find_column_index(values, event_name, name)
    range_to_update = f"Event Attendance!{ALPHABET[alpha_index]}{index}"
    body = {
        "values": [[f"{name}"]]
    }
    get_build().spreadsheets().values().update(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()
