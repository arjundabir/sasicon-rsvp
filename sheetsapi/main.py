import os
from dotenv import load_dotenv

# pylint: disable=import-error
from google_auth.credentials import get_build
from form_response.form_response import FormResponse, get_form_responses, init_email_sent
from event_attendance.add_to_event import add_to_event

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_RESPONSES_RANGE = os.getenv("FORM_RESPONSES_RANGE")


def handle_new_form_response(service, i, row):
    form_response = FormResponse(row)
    init_email_sent(service, i, row)
    add_to_event(service, event_name="test",
                 name=form_response.name, email=form_response.email)
    form_response.email_sent = False
    print(form_response.to_dict())


def main():
    service = get_build()
    form_response_values = get_form_responses(service)

    if not form_response_values:
        print("No data found.")
        return

    # the first row is the header, so we skip it
    for i, row in enumerate(form_response_values[1:]):
        form_response = FormResponse(row)

        if not form_response.email_sent:
            handle_new_form_response(service, i, row)


if __name__ == "__main__":
    main()
