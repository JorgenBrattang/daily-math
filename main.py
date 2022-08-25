import scope
from random import randint
from datetime import date


def welcome():
    """
    Welcomes you to the game
    """
    message = """
    Welcome player, please login and enjoy your daily math.
    If you need help with your questions just follow the
    instructions while they are presented.
    Now enjoy your stay!
    """
    print(message)


# Sets up the variables
# wks = worksheet
users_wks = scope.SHEET.worksheet("users")
quotes_wks = scope.SHEET.worksheet("quotes")


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
        # Access the pin code from google sheet with usernames
        pin_code = int(users_wks.cell(user_cell.row, 2).value)
        if pin_code == user_pin:
            success_login(username)
        else:
            print("Pin code and does not match!")
            # Asks for the pin code if it was not the same
            while True:
                is_this_you = input(f"Are you {username}? Enter Y or N: ")
                # if yes, user get another chance to enter a correct pin number
                if is_this_you.lower() == "y":
                    user_pin = int(create_user_pin())
                    if pin_code == user_pin:
                        success_login(username)
                        break
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
        print(f"\nYour account is setup {username}\nPlease proceed to login\n")
        check_if_exists()


def failed_login(username, user_pin):
    """
    If you entered the wrong pin code, print wrong pin and
    you entered wrong pin code.
    """
    print(f"\nWrong pin code for {username}, try again")
    print(f"\nYou entered pin code {user_pin}")


def success_login(username):
    """
    If you entered the right pin code, print successfull login.
    """
    welcome_to_daily_math(username)
    latest_login(username)


def date_today():
    """
    Gives you the todays date with this format: August 25, 2022
    """
    return date.today().strftime("%B %d, %Y")


def latest_login(username):
    """
    Sets the date you latest logged in.
    """
    # Finds the user
    user_cell = users_wks.find(username, in_column=1)
    # Selects the row
    row_select = user_cell.row
    message = "You have 5 points left to complete the day"
    # checks the value of date in google sheets
    users_latest_login = users_wks.cell(row_select, 3).value
    if date_today() == users_latest_login:
        # Print out a message how many points are left for today.
        print(f"\n{message}: 5")
    else:
        # Print and (soon) sets the number of points are left.
        print(f"\n{message}: 15")
        # Updates the date cell with todays date
        users_wks.update_cell(row_select, 3, date_today())


def welcome_to_daily_math(username):
    """
    Welcome you to daily math and gives random motivational qoute.
    """
    print(f"\nWelcome to Daily Math {username}, may your calculations be true!\n")
    print(f"Todays date is: {date_today()}\n")
    random_qoutes()


def random_qoutes():
    """
    Gives you an random qoute from google sheets
    """
    length = quotes_wks.row_count
    random_number = randint(2, length)
    qoutes = quotes_wks.cell(random_number, 1).value
    author = quotes_wks.cell(random_number, 2).value
    print(f"{qoutes}\n    - {author}")


def start():
    """
    Starts the program
    """
    welcome()
    check_if_exists()


start()
