"""handles form responses sheet"""
# pylint: disable=import-error
from get_env import get_env


class FormResponse:
    """represents a form response"""

    def __init__(self, row):
        self.row = row
        self.timestamp = row[0]
        self.firstname = row[1]
        self.lastname = row[2]
        self.school_email = row[3]
        self.graduation_year = row[4]
        self.majors = row[5]
        self.email = row[6]
        self.food_preferences = row[7]
        self.email_sent = row[8] if len(row) > 8 else ""

    def to_dict(self):
        """returns a dictionary representation of the form response"""
        return {
            "timestamp": self.timestamp,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "name": self.name(),
            "school_email": self.school_email,
            "graduation_year": self.graduation_year,
            "majors": self.majors,
            "email": self.email,
            "email_sent": self.email_sent,
        }

    def name(self):
        """returns the name of the form response"""
        return f"{self.firstname} {self.lastname}"


def get_form_responses(service):
    """returns the form responses from the spreadsheet"""
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=get_env()[0],
            range=get_env()[1],
            majorDimension="ROWS",
        )
        .execute()
    )
    return result.get("values", [])


def init_email_sent(service, row_index, row):
    """initializes the email sent column to false"""
    range_to_update = f"Form Responses 1!H{row_index + 1}"
    body = {
        "values": [[False]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=get_env()[0],
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()
