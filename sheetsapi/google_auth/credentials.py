"""
This module contains the function to get credentials from token.json
"""
import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_credentials():
    """gets credentials from token.json"""

    path_to_token = os.path.join(os.path.dirname(__file__), "token.json")

    creds = None
    if os.path.exists(path_to_token):
        creds = Credentials.from_authorized_user_file(
            path_to_token, SCOPES)
    return creds


def get_build():
    """gets the build object"""
    return build("sheets", "v4", credentials=get_credentials())
