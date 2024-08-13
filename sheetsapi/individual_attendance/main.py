"""
handles the individual attendance spreadsheet
"""
# pylint: disable=import-error
from get_env import get_env

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def add_to_individual_attendance(service, name):
    """
    Adds the form response to the individual attendance spreadsheet
    """
    values = get_values(service)
    alpha_index, index = find_column_index(values, name)

    if alpha_index == -1:
        create_column(service, name, len(values))
        values = get_values(service)
        alpha_index, index = find_column_index(values, name)

    else:
        add_to_column(service, name, alpha_index, index)


def add_to_column(service, name, alpha_index, index):
    """
    Adds the form response to the column in the individual attendance spreadsheet
    """
    range_to_update = f"Individual Attendance!{ALPHABET[alpha_index]}{index}"
    sheet = service.spreadsheets()
    body = {
        "values": [[name]]
    }
    sheet.values().append(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()


def get_values(service):
    """
    Gets the values from the individual attendance spreadsheet
    """
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=get_env()[0],
        range=get_env()[3],
        majorDimension="COLUMNS",
    ).execute()
    return result.get("values", [])


def find_column_index(values, name):
    """
    Finds the column index of the name in the individual attendance spreadsheet
    """
    for i, column in enumerate(values):
        if column[0] == name:
            return i, len(column) + 1
    return -1, -1


def create_column(service, name, alpha_index):
    """
    Creates a new column for the name in the individual attendance spreadsheet
    """
    range_to_update = f"Individual Attendance!{ALPHABET[alpha_index]}{1}"
    sheet = service.spreadsheets()
    body = {
        "values": [[name]]
    }
    sheet.values().append(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()
