import os
from dotenv import load_dotenv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from credentials import get_credentials
from form_responses import FormResponse, get_form_responses, init_email_sent
# Import the update_attendance function
from attendance import update_attendance

load_dotenv()


SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_RESPONSES_RANGE = os.getenv("FORM_RESPONSES_RANGE")


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
                init_email_sent(service, i, row)
                form_response.email_sent = False

                # Combine first and last name into one cell and mark "conference"
                attendance_row = [
                    f"{form_response.firstname} {form_response.lastname}"]
                update_attendance(service, i, attendance_row)

            print(f"Inserted: {form_response.to_dict()}")

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
