# pylint: disable=import-error
from get_env import get_env


def add_to_event(service, event_name, name, email):
    # pylint: disable=no-member
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=get_env()[0],
        range=get_env()[2],
        majorDimension="ROWS",
    ).execute()
    return result.get("values", [])
