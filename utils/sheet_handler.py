import logging
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
from config import SCOPE, CREDS_FILE, SPREADSHEET_ID

def get_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).sheet1

def chunked(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
