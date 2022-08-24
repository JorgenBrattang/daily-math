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


users_worksheet = SHEET.worksheet("users")


def create_user_name():
    """ Creates new user name """
    return input("Enter your name: ")


def create_user_pin():
    """ Creates new user pin code """
    return input("Enter your pin code: ")


def update_users_worksheet(user_name, pin_code):
    """
    Creates a list from the user inputs and updates the
    google sheet with the user input from
    functions create_user_name() and create_user_pin()
    """
    create_list = [user_name, pin_code]
    users_worksheet.append_row(create_list)


def main():
    """
    Runs the programs functions.
    """
    user_str = create_user_name()
    pin_int = create_user_pin()
    update_users_worksheet(user_str, pin_int)
    data = users_worksheet.get_all_values()
    print(data)


main()

