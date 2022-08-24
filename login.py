import scope
import success_login


# Sets up the variables
# wks = worksheet
users_wks = scope.SHEET.worksheet("users")


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
    Checks if the name already exists and tests the pin code, and
    if it doesn't exists, creates a new user.
    """
    username = create_username()
    user_pin = int(create_user_pin())
    user_cell = users_wks.find(username, in_column=1)
    if user_cell is not None:
        print("The user name exists")
        # Access the pin code from google sheet with usernames
        pin_code = int(users_wks.cell(user_cell.row, 2).value)
        if pin_code == user_pin:
            success_login.success_login(username)
        else:
            print("Pin code and does not match!")
            # Asks for the pin code if it was not the same
            while True:
                is_this_you = input(f"Are you {username}? Enter Y or N: ")
                # if yes, user get another chance to enter a correct pin number
                if is_this_you.lower() == "y":
                    user_pin = int(create_user_pin())
                    if pin_code == user_pin:
                        success_login.success_login(username)
                    else:
                        failed_login(username, user_pin)
                # If no, repeat the step above to enter a new username and pin
                elif is_this_you.lower() == "n":
                    check_if_exists()
                    break
                else:
                    print(f"\nPlease {username}, enter the key Y or N")
    else:
        # If the user name does not exist do this:
        update_users_worksheet(username, user_pin)
        print(f"\nSuccessfully created account: {username}")


def failed_login(username, user_pin):
    """
    If you entered the wrong pin code, print wrong pin and
    you entered wrong pin code.
    """
    print(f"\nWrong pin code for {username}, try again")
    print(f"\nYou entered pin code {user_pin}")
