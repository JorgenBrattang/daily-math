import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('daily-math')


def create_user():
    """ Creates new user """
    print("Create your login name: ")
    user_str = input("Enter your name: ")
    print(f"The chosen name is {user_str}\n")

    print("Create your pin code: ")
    pin_code = input("Enter your pin code: ")
    print(f"The chosen pin code is {pin_code}")


create_user()