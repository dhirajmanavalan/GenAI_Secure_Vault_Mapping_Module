import json
import os
import pickle
import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_credentials():
    creds = None

    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.pkl", "wb") as token:
            pickle.dump(creds, token)

    return creds


def connect_sheet():
    creds = get_credentials()
    client = gspread.authorize(creds)
    return client.open("Test_Report").sheet1

def parse_report():
    with open("reports/report.json") as f:
        data = json.load(f)

    rows = []

    for i, test in enumerate(data["tests"], start=1):
        status = "PASS" if test["outcome"] == "passed" else "FAIL"

        rows.append([
            f"TC-{i:02}",
            test["nodeid"],
            "Good",
            status,
            status,
            "Dhiraj"
        ])

    return rows


def update_sheet():
    sheet = connect_sheet()
    rows = parse_report()

    for row in rows:
        sheet.append_row(row)


if __name__ == "__main__":
    update_sheet()