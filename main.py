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
# wks = worksheet
users_wks = SHEET.worksheet("users")
data = users_wks.get_all_values()


def create_username():
    """ Creates new user name """
    user_input = input("Enter your name: ")
    return user_input.lower()


def create_user_pin():
    """ Creates new user pin code """
    return int(input("Enter your pin code: "))


def update_users_worksheet(user_name, pin_code):
    """
    Creates a list from the user inputs and updates the
    google sheet with the user input from
    functions create_user_name() and create_user_pin()
    """
    create_list = [user_name, pin_code]
    users_wks.append_row(create_list)


def check_if_exists():
    """
    Checks if the name already exists
    """
    username = create_username()
    user_pin = int(create_user_pin())
    user_cell = users_wks.find(username, in_column=1)
    if user_cell is not None:
        print("The user name exists")
        # Access the pin code from google sheet with usernames 
        pin_code = int(users_wks.cell(user_cell.row, 2).value)
        print(f"\nSearched type: {type(pin_code)}")
        print(f"Searched value: {pin_code}")
        print(f"\nThis your input type: {type(user_pin)}")
        print(f"This your input pin: {user_pin}\n")
        if pin_code is user_pin:
            print("Successfull login")
        else:
            print("Pin code and does not match!")
        
        # else:
        #     return create_username()
    else:
        return username


def main():
    """
    Runs the programs functions.
    """
    check_if_exists()
    # user_str = check_if_exists()
    # pin_int = create_user_pin()
    # update_users_worksheet(user_str, pin_int)


main()
