from random import randint
from datetime import date
from rich.console import Console
from readchar import readkey, key
from time import sleep
import os
import scope
console = Console()


# wks = worksheet
users_wks = scope.SHEET.worksheet("users")
quotes_wks = scope.SHEET.worksheet("quotes")
questions_1_wks = scope.SHEET.worksheet("questions-1")
questions_2_wks = scope.SHEET.worksheet("questions-2")
questions_3_wks = scope.SHEET.worksheet("questions-3")


# -------- Credit code ----------
def clear_screen():
    """ 
    Clears the screen when called.
    Credits: https://teamtreehouse.com/community/using-a-clearscreen-in-pycharm
    """
    os.system('cls' if os.name == 'nt' else 'clear')
# -------- ........... ----------


def center_text(message):
    """ Center the text """
    length = 79 - (len(message))
    console.print(message.center(len(message) + length))


def space_top():
    """ Creates 5 break lines when called """
    for x in range(5):
        print("")


def input_message():
    """ Enter here string """
    return "                           Enter here: "


def new_screen():
    """ Starts new screen """
    clear_screen()
    space_top()
    sleep(0.5)


def welcome_message():
    """
    Welcomes you to the game
    """
    new_screen()
    center_text("Welcome player, please login and enjoy your daily math.")


def ask_new_user():
    """ Ask if you are a new user """
    new_user = True
    while True:
        sleep(0.5)
        center_text("Are you a new user? Y or N")
        k = readkey()
        if k == "y":
            clear_screen()
            check_if_exists(new_user)
            break
        elif k == "n":
            clear_screen()
            new_user = False
            check_if_exists(new_user)
            break
        elif k != "y":
            clear_screen()
            space_top()
            center_text("Press Y for yes and N for no")


def create_username():
    """ Creates new user name """
    new_screen()
    center_text("Enter a name, use only letters.")
    while True:
        sleep(0.5)
        username = input(input_message())
        if username.isalpha():
            if len(username) > 15:
                clear_screen()
                center_text("To many characters, please limit yourself to 15.")
            else:
                return username.lower()
                break
        sleep(1)
        clear_screen()
        space_top()
        center_text("Please try again")
        sleep(1)
        center_text("Also only alphabetic characters allowed.")


def create_user_pin():
    """ Creates new user pin code """
    new_screen()
    center_text("Please enter a 4 digit pin code")
    while True:
        try:
            sleep(0.5)
            user_pin = int(input(input_message()))
            test_pin_lenght = len(str(user_pin))
            if test_pin_lenght == 4:
                return user_pin
                break
            else:
                raise ValueError
        except ValueError:
            clear_screen()
            space_top()
            sleep(1)
            center_text("That's not a valid option!")
            sleep(1)
            center_text("Use 4 digits to create a pin code")


def create_birth_year():
    """ Creates new user age """
    new_screen()
    center_text("Please enter a 4 digit year of birth")
    while True:
        try:
            sleep(0.5)
            birth_year = int(input(input_message()))
            test_pin_lenght = len(str(birth_year))
            if test_pin_lenght == 4:
                return birth_year
                break
            else:
                raise ValueError
        except ValueError:
            clear_screen()
            space_top()
            sleep(1)
            center_text("That's not a valid option!")
            sleep(1)
            center_text("Use 4 digits to create year of birth")


def update_users_worksheet(user_name, user_pin, birth_year, date_time):
    """
    Creates a list from the user inputs and updates the
    google sheet with the user input from
    functions create_user_name() and create_user_pin()
    """
    create_list = [user_name, user_pin, birth_year, date_time]
    users_wks.append_row(create_list)


def check_if_exists(new_user):
    """
    Checks if the name already exists and tests the pin code, and
    if it doesn't exists, creates a new user.
    """
    while True:
        # Defines the username from the function
        username = create_username()
        # Checks the users wks for the username
        user_cell = users_wks.find(username, in_column=1)
        # If it doesn't exist
        if user_cell is not None:
            if new_user is True:
                print("")
                center_text("This exists already, try another.")
                sleep(3)
                clear_screen()
            # new_user is False
            else:
                break
        # If it does exist
        else:
            # If the user cell dont exist
            if user_cell is None:
                # And new_user is True
                if new_user is True:
                    break
                # Or if new_user is False,
                # So it's and existing user trying to login
                else:
                    center_text("This account don't exist")
                    # ----------------------------------- Make function later
                    while True:
                        question_user = input("Try again? Enter Y or N: ")
                        print("")
                        if question_user.lower() == "y":
                            check_if_exists(False)
                            break
                        elif question_user.lower() == "n":
                            menu(username)
                        else:
                            print("")
                            print("Please enter the key Y or N.")
                    # ----------------------------------- Make function later
            else:
                break
    user_pin = create_user_pin()
    if user_cell is not None:
        # Access the pin code from google sheet with usernames
        pin_code = int(users_wks.cell(user_cell.row, 2).value)
        if pin_code == user_pin:
            success_login(username)
    else:
        # If the user name does not exist do this:
        birth_year = create_birth_year()
        update_users_worksheet(username, user_pin, birth_year, date_today())
        reset_treats(username)
        new_screen()
        center_text("Your account is setup")
        center_text("Please proceed to login\n")
        press_any_key()
        check_if_exists(False)


def press_any_key():
    """ Press any key to continue """
    center_text("Press any key to continue...")
    while True:
        k = readkey()
        if k == key.ENTER:
            new_screen()
            break
        if k != key.ENTER:
            new_screen()
            break


def welcome_to_daily_math(username):
    """
    Welcome you to daily math and gives random motivational qoute.
    """
    new_screen()
    center_text("Welcome to Daily Math " + make_capitalize(username))
    center_text("May your calculations be true!")
    center_text("Todays date is: " + date_today())
    print("")
    press_any_key()
    random_qoutes()
    print("")
    press_any_key()


def latest_login(username):
    """
    Checks if the latest date you logged in match todays, and if
    not it changes it to today.
    """
    # Finds the users row
    row_select = find_user(username)
    # checks the value of date in google sheets
    users_latest_login = users_wks.cell(row_select, 4).value
    test = "5"
    message = "You need " + test + " treats to complete this day!"
    print("")
    if date_today() == users_latest_login:
        # Print out a message how many points are left for today.
        center_text(message)
        menu(username)
    else:
        # Print and (soon) sets the number of points are left.
        center_text(f"\n{message}: 15\n")
        # Updates the date cell with todays date
        users_wks.update_cell(row_select, 4, date_today())
        reset_treats(username)
        menu(username)


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


def find_user(username):
    """
    Finds the user from the google sheet.
    """
    # Finds the user
    user_cell = users_wks.find(username, in_column=1)
    # Selects the row
    return user_cell.row


def random_qoutes():
    """
    Gives you an random qoute from google sheets
    """
    length = quotes_wks.row_count
    random_number = randint(2, length)
    qoutes = quotes_wks.cell(random_number, 1).value
    author = quotes_wks.cell(random_number, 2).value
    center_text(f"{qoutes}\n    - {author}")
 

def calculate_age(username):
    """
    This calculates your age based on your of birth and todays date.
    """
    year_now = date.today().strftime("%Y")
    row_select = find_user(username)
    year_of_birth = users_wks.cell(row_select, 3).value
    return (int(year_now)) - (int(year_of_birth))


def instructions(username):
    """
    Prints the instructions for the difficulty levels
    """
    print("")
    message = "you now have three choices of difficulty"
    center_text(f"{make_capitalize(username)} {message}")
    center_text("1. Age 3-5")
    center_text(" 2. Age 6-12")
    center_text("3. Age 12+")


def random_questions(num):
    """
    Random question
    """
    if num == 1:
        worksheet = questions_1_wks
    elif num == 2:
        worksheet = questions_2_wks
    elif num == 3:
        worksheet = questions_3_wks
    print("")
    length = worksheet.row_count
    random_number = randint(2, length)
    question = worksheet.cell(random_number, 1).value
    answer = worksheet.cell(random_number, 2).value
    return [question, answer]


def answer_question(username, num):
    """
    Here you will get to answer the question given to you.
    """
    question_list = random_questions(num)
    tries = 0
    while True:
        print("")
        print(question_list[0])
        while True:
            user_input = input("Enter your answer here: ")
            if user_input.find(".") > 0:
                center_text("Your answer contains a dot (.), please use commas (,)")
            else:
                break
        if user_input == question_list[1]:
            center_text(f"That is correct {make_capitalize(username)}, good work!")
            earn_treats(username)
            another_question(username, num)
            break
        else:
            tries += 1
            if tries == 3:
                while True:
                    print("")
                    center_text("Press 1 for solution.")
                    center_text("Press 2 for to keep trying.")
                    choice_input = int(input("Enter number here: "))
                    if choice_input == 1:
                        print("")
                        center_text(f"The answer is {question_list[1]}")
                        another_question(username, num)
                    elif choice_input == 2:
                        answer_question(username, num)
                    else:
                        message = "Pick a number between 1 and 2!"
                        not_that_hard(username)
                        center_text(message)
            print(tries)
            print(f"\nWrong answer, keep trying {make_capitalize(username)}!")


def not_that_hard(username):
    """ Prints out not that hard and username """
    center_text(f"\nIt's not that hard {make_capitalize(username)}...")


def another_question(username, num):
    """
    Asks if you want another question in the same difficulty
    """
    print("")
    while True:
        print("")
        user_input = input("Do you want to continue? Enter Y or N: ")
        if user_input.lower() == "y":
            answer_question(username, num)
            break
        elif user_input.lower() == "n":
            print("")
            menu(username)
            break
        else:
            center_text(f"\nPlease {username}, enter the key Y or N")


def make_capitalize(username):
    """
    Makes the username uppercase for readability.
    """
    return username.capitalize()


def choose_difficulty(username):
    """
    Here you get a choice to choose your difficulty level
        - Age 3-5
        - Age 6-12
        - Age 12+
    """
    your_age = calculate_age(username)
    instructions(username)
    choice_input = int(input("Pick a number between 1 and 3: "))
    if choice_input == 1:
        num = 1
        if your_age > 5:
            # ----------------------------------- Make function later
            print("")
            print(f"Your age is {your_age}, this is for age 3-5.")
            print("But if you really wanna do it, go ahead, I believe in you!")
            while True:
                print("")
                user_input = input("Are you sure? Enter Y or N: ")
                if user_input.lower() == "y":
                    answer_question(username, num)
                    break
                elif user_input.lower() == "n":
                    print("")
                    choose_difficulty(username)
                    break
                else:
                    center_text(f"\nPlease {username}, enter the key Y or N")
            # ----------------------------------- Make function later
        else:
            answer_question(username, num)
    elif choice_input == 2:
        num = 2
        if your_age > 13:
            # ----------------------------------- Make function later
            print("")
            center_text(f"Your age is {your_age}, this is for age 6-12.")
            center_text("But if you really wanna do it, go ahead, I believe in you!")
            while True:
                print("")
                user_input = input("Are you sure? Enter Y or N: ")
                if user_input.lower() == "y":
                    answer_question(username, num)
                    break
                elif user_input.lower() == "n":
                    print("")
                    choose_difficulty(username)
                    break
                else:
                    center_text(f"\nPlease {username}, enter the key Y or N")
            # ----------------------------------- Make function later
        else:
            answer_question(username, num)
    elif choice_input == 3:
        num = 3
        answer_question(username, num)
    else:
        message = "Pick a number between 1 and 3!"
        center_text(f"\nIt's not that hard {make_capitalize(username)}...")
        center_text(f"{message}\n")
        choose_difficulty(username)


def earn_treats(username):
    """
    Give the user treats for each completed question.
    """
    # Finds the users row
    row_select = find_user(username)
    # checks the value of treats in google sheets
    users_treats = users_wks.cell(row_select, 5).value
    # Sets the users_treats to be int and adds more readability
    increase_treats = int(users_treats)
    # Access the users worksheets and increases the treats by 1
    users_wks.update_cell(row_select, 5, increase_treats+1)


def reset_treats(username):
    """
    Resets the users treats for a new day.
    """
    # Finds the users row
    row_select = find_user(username)
    # Access the users worksheets and sets the treats back to 0
    users_wks.update_cell(row_select, 5, 0)


def login_screen():
    """
    First thing you see and that you need to login / register to move on.
    """
    welcome_message()
    ask_new_user()


def menu(username):
    """
    This is where you return to when your done with certain things
    """
    center_text("Menu, press the number to continue")
    center_text("1. Question")
    center_text("2. Motivational quote")
    center_text("3. Quit")
    while True:
        k = readkey()
        if k == "1":
            choose_difficulty(username)
        elif k == "2":
            clear_screen()
            space_top()
            random_qoutes()
            press_any_key()
            menu(username)
        elif k == "3":
            print("")
            center_text("Are you sure? Y or N")
            while True:
                k = readkey()
                if k == "y":
                    quit()
                elif k == "n":
                    clear_screen()
                    menu(username)
                elif k != "y":
                    clear_screen()
                    space_top()
                    center_text("Press Y for yes and N for no")
        else:
            print("Did not press 1, 2 or 3.. Try again")


login_screen()
# menu("test")
