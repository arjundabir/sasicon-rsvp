"""
This module contains the function to get credentials from token.json
"""
import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_credentials():
    """gets credentials from token.json"""

    creds = None
    if os.path.exists("./google_auth/token.json"):
        creds = Credentials.from_authorized_user_file(
            "./google_auth/token.json", SCOPES)
    return creds


def get_build():
    """gets the build object"""
    return build("sheets", "v4", credentials=get_credentials())
