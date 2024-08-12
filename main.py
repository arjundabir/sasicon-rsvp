import os
from dotenv import load_dotenv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from credentials import get_credentials

load_dotenv()


SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_RESPONSES_RANGE = os.getenv("FORM_RESPONSES_RANGE")


class FormResponse:
    def __init__(self, row):
        self.row = row
        self.timestamp = row[0]
        self.firstname = row[1]
        self.lastname = row[2]
        self.school_email = row[3]
        self.graduation_year = row[4]
        self.majors = row[5]
        self.email = row[6]
        self.email_sent = row[7] if len(row) > 7 else ""

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "school_email": self.school_email,
            "graduation_year": self.graduation_year,
            "majors": self.majors,
            "email": self.email,
            "email_sent": self.email_sent,
        }


def update_spreadsheet(service, row_index, row):
    range_to_update = f"Form Responses 1!H{row_index + 1}"
    body = {
        "values": [[False]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()


def get_form_responses(service):
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=FORM_RESPONSES_RANGE,
            majorDimension="ROWS",
        )
        .execute()
    )
    return result.get("values", [])


def main():
    creds = get_credentials()

    try:
        service = build("sheets", "v4", credentials=creds)
        values = get_form_responses(service)

        if not values:
            print("No data found.")
            return

        # the first row is the header, so we skip it
        for i, row in enumerate(values[1:], start=1):
            form_response = FormResponse(row)
            if not form_response.email_sent:
                update_spreadsheet(service, i, row)
                form_response.email_sent = "FALSE"
            print(f"Inserted: {form_response.to_dict()}")

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
