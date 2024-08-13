"""handles the logic for the attendance sheet"""
from get_env import get_env


def get_attendance(service):
    """returns the attendance from the spreadsheet"""
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=get_env()[0],
            range="Attendance!A1:Z",  # Specify a complete range
            majorDimension="COLUMNS",
        )
        .execute()
    )
    return result.get("values", [])


def update_attendance(service, row):
    """updates the attendance in the next empty column of the spreadsheet"""
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=get_env()[0],
        range="Attendance!A1:Z1",  # Check the first row for the next empty column
        majorDimension="ROWS"
    ).execute()
    values = result.get("values", [])
    # Determine the next empty column
    next_empty_col = len(values[0]) + 1 if values else 1

    range_to_update = f"Attendance!{chr(64 + next_empty_col)}1:{chr(64 + next_empty_col)}"
    body = {
        "values": [row]
    }
    service.spreadsheets().values().update(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body,
    ).execute()


def add_attendance():
