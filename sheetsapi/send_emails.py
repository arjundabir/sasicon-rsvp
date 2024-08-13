# pylint: disable=import-error
from get_env import get_env
from google_auth.credentials import get_build
from form_response.form_response import get_form_responses
from form_response.form_response import FormResponse
from generate_qrcode.main import generate_qrcode
from emailer.main import send_email

SPREADSHEET_ID = get_env()[0]
FORM_RESPONSES_RANGE = get_env()[1]


def update_email_sent(service, row_index):
    """
    updates the email sent column to true
    """
    range_to_update = f"Form Responses 1!I{row_index + 1}"
    body = {
        "values": [[True]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_to_update,
        valueInputOption="RAW",
        body=body
    ).execute()


if __name__ == "__main__":
    service = get_build()
    form_response_values = get_form_responses(service)

    if not form_response_values:
        print("No data found.")

    for i, row in enumerate(form_response_values[1:], start=1):
        form_response = FormResponse(row)
        if not form_response.email_sent:
            qr_code_file = generate_qrcode(form_response.name())
            send_email(form_response, qr_code_file)
            update_email_sent(service, i)
