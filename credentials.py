"""
This module contains the function to get credentials from token.json
"""
import os.path

from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_credentials():
    """gets credentials from token.json"""

    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    return creds
