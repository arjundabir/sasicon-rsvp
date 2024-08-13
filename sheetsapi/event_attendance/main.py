# pylint: disable=import-error
from get_env import get_env

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_values(service):
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


def create_event_column(service, event_name):
    """
    Creates a new column for the event in the spreadsheet
    """
    # pylint: disable=no-member
    sheet = service.spreadsheets()
    body = {
        "values": [[event_name]]
    }
    sheet.values().append(
        spreadsheetId=get_env()[0],
        range=get_env()[2],
        valueInputOption="RAW",
        body=body
    ).execute()


def add_to_event(service, event_name, name):
    """
    Adds attendees name under event in the spreadsheet
    """
    # pylint: disable=no-member
    values = get_values(service)
    alpha_index, index = find_column_index(values, event_name, name)

    # if the name is already in the event, we don't need to do anything
    if alpha_index == -2:
        return

    if alpha_index == -1:
        create_event_column(service, event_name)

        values = get_values(service)
        alpha_index, index = find_column_index(values, event_name, name)
    range_to_update = f"Event Attendance!{ALPHABET[alpha_index]}{index}"
    body = {
        "values": [[f"{name}"]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()
