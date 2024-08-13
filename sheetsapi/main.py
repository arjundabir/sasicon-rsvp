import os
from dotenv import load_dotenv

from google_auth.credentials import get_build
from form_response.form_response import FormResponse, get_form_responses

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_RESPONSES_RANGE = os.getenv("FORM_RESPONSES_RANGE")


def main():
    service = get_build()
    values = get_form_responses(service)

    if not values:
        print("No data found.")
        return

    # the first row is the header, so we skip it
    for row in values[1:]:
        form_response = FormResponse(row)
        print(form_response.to_dict())


if __name__ == "__main__":
    main()
