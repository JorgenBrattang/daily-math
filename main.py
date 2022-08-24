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

# Sets up the variables
users_worksheet = SHEET.worksheet("users")
data = users_worksheet.get_all_values()


def create_user_name():
    """ Creates new user name """
    user_input = input("Enter your name: ")
    return user_input.lower()


def create_user_pin():
    """ Creates new user pin code """
    return input("Enter your pin code: ")


def update_users_worksheet(user_name, pin_code):
    """
    Creates a list from the user inputs and updates the
    google sheet with the user input from
    functions create_user_name() and create_user_pin()
    """
    # create_list = [user_name, pin_code]
    check_if_exists(user_name)
    # users_worksheet.append_row(create_list)


def check_if_exists(user_name):
    """
    Checks the google sheet if the user already exists.
    """
    cell = users_worksheet.find(user_name, in_column=1)
    if cell is not None:
        print("Your selected username exists, please try another")
    else:
        print("Does not exists, continue to create pin number")


def main():
    """
    Runs the programs functions.
    """
    # user_str = create_user_name()
    # pin_int = create_user_pin()
    # update_users_worksheet(user_str, pin_int)


# main()
check_if_exists("not")
