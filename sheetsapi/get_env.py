"""handles the environment variables"""
import os
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_RESPONSES_RANGE = os.getenv("FORM_RESPONSES_RANGE")
ATTENDANCE_RANGE = os.getenv("ATTENDANCE_RANGE")


def get_env():
    """returns the environment variables"""
    return SPREADSHEET_ID, FORM_RESPONSES_RANGE, ATTENDANCE_RANGE
