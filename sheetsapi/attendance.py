"""handles the logic for the attendance sheet"""
from get_env import get_env


def get_attendance(service):
    """returns the attendance from the spreadsheet"""
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=get_env()[0],
            range=get_env()[2],
            majorDimension="ROWS",
        )
        .execute()
    )
    return result.get("values", [])


def update_attendance(service, row_index, row):
    """updates the attendance in the spreadsheet"""
    range_to_update = f"Attendance!A{row_index + 1}"
    body = {
        "values": [row]
    }
    service.spreadsheets().values().update(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()
