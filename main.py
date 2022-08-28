""" Imports """
from random import randint
from datetime import date
from readchar import readkey, key
import scope

# Sets up the variables
# wks = worksheet
users_wks = scope.SHEET.worksheet("users")
quotes_wks = scope.SHEET.worksheet("quotes")
questions_1_wks = scope.SHEET.worksheet("questions-1")
questions_2_wks = scope.SHEET.worksheet("questions-2")
questions_3_wks = scope.SHEET.worksheet("questions-3")


def welcome_message():
    """
    Welcomes you to the game
    """
    message = """
    Welcome player, please login and enjoy your daily math.
    """
    print(message)


def ask_new_user():
    """ Ask if you are a new user """
    print("Are you a new user?")
    new_user = True
    # ----------------------------------- Make function later
    while True:
        question_user = input("Enter Y or N: ")
        print("")
        if question_user.lower() == "y":
            check_if_exists(new_user)
            break
        elif question_user.lower() == "n":
            new_user = False
            check_if_exists(new_user)
            break
        else:
            print("")
            print("Please enter the key Y or N.")
    # ----------------------------------- Make function later


def create_username():
    """ Creates new user name """
    while True:
        username = input("Enter your name: ")
        if username.isalpha():
            return username.lower()
            break
        print("Incorrect name, only letters allowed. Please try again")


def create_birth_year():
    """ Creates new user age """
    print("")
    print("Please enter a 4 digit year of birth")
    while True:
        birth_year = int(input("Enter your year of birth: "))
        length = len(str(birth_year))
        if length == 4:
            return birth_year
            break
        print("Incorrect year of birth. Please try again")


def create_user_pin():
    """ Creates new user pin code """
    print("")
    print("Please enter a 4 digit pin code")
    while True:
        birth_year = int(input("Enter your pin code: "))
        length = len(str(birth_year))
        if length == 4:
            return birth_year
            break
        print("Incorrect pin code. Please try again")


def update_users_worksheet(user_name, pin_code, birth_year, date_time):
    """
    Creates a list from the user inputs and updates the
    google sheet with the user input from
    functions create_user_name() and create_user_pin()
    """
    create_list = [user_name, pin_code, birth_year, date_time]
    users_wks.append_row(create_list)


def check_if_exists(*args):
    """
    Checks if the name already exists and tests the pin code, and
    if it doesn't exists, creates a new user.
    """
    while True:
        # Gets the argument new_user which holds True or False
        for arg in args:
            new_user = arg
        # Defines the username from the function
        username = create_username()
        # Checks the users wks for the username
        user_cell = users_wks.find(username, in_column=1)
        # If it doesn't exist
        if user_cell is not None:
            if new_user is True:
                print("This exists already, try another.")
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
                    print("This account don't exist")
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
    user_pin = int(create_user_pin())
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
        print(f"\nYour account is setup {make_capitalize(username)}")
        print("Please proceed to login\n")
        check_if_exists(False)


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


def latest_login(username):
    """
    Checks if the latest date you logged in match todays, and if
    not it changes it to today.
    """
    # Finds the users row
    row_select = find_user(username)
    # checks the value of date in google sheets
    users_latest_login = users_wks.cell(row_select, 4).value
    message = "You got 5 points left to complete the day"
    if date_today() == users_latest_login:
        # Print out a message how many points are left for today.
        print(f"\n{message}: 5\n")
        menu(username)
    else:
        # Print and (soon) sets the number of points are left.
        print(f"\n{message}: 15\n")
        # Updates the date cell with todays date
        print("This is working.. kinda")
        users_wks.update_cell(row_select, 4, date_today())
        reset_treats(username)
        menu(username)


def welcome_to_daily_math(username):
    """
    Welcome you to daily math and gives random motivational qoute.
    """
    print(f"\nWelcome to Daily Math {make_capitalize(username)}")
    print("May your calculations be true!")
    print("")
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
    print(f"{make_capitalize(username)} {message}")
    print("    1. Age 3-5")
    print("    2. Age 6-12")
    print("    3. Age 12+")


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
        user_input = input("Enter your answer here: ")
        # if user_input -------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if user_input == question_list[1]:
            print(f"That is correct {make_capitalize(username)}, good work!")
            earn_treats(username)
            another_question(username, num)
            break
        else:
            tries += 1
            if tries == 3:
                while True:
                    print("")
                    print("Press 1 for solution.")
                    print("Press 2 for to keep trying.")
                    choice_input = int(input("Enter number here: "))
                    if choice_input == 1:
                        print("")
                        print(f"The answer is {question_list[1]}")
                        another_question(username, num)
                    elif choice_input == 2:
                        answer_question(username, num)
                    else:
                        message = "Pick a number between 1 and 2!"
                        not_that_hard(username)
                        print(message)
            print(tries)
            print(f"\nWrong answer, keep trying {make_capitalize(username)}!")


def not_that_hard(username):
    """ Prints out not that hard and username """
    print(f"\nIt's not that hard {make_capitalize(username)}...")


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
            print(f"\nPlease {username}, enter the key Y or N")


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
                    print(f"\nPlease {username}, enter the key Y or N")
            # ----------------------------------- Make function later
        else:
            answer_question(username, num)
    elif choice_input == 2:
        num = 2
        if your_age > 13:
            # ----------------------------------- Make function later
            print("")
            print(f"Your age is {your_age}, this is for age 6-12.")
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
                    print(f"\nPlease {username}, enter the key Y or N")
            # ----------------------------------- Make function later
        else:
            answer_question(username, num)
    elif choice_input == 3:
        num = 3
        answer_question(username, num)
    else:
        message = "Pick a number between 1 and 3!"
        print(f"\nIt's not that hard {make_capitalize(username)}...")
        print(f"{message}\n")
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
    print("Menu, select what you want to do.")
    print("1. Question")
    print("2. Motivational quote")
    print("3. Quit")
    while True:
        user_input = input("Enter number here: ")
        integer = user_input.isnumeric()
        if integer is True:
            if user_input == "1":
                choose_difficulty(username)
                quit()
            elif user_input == "2":
                random_qoutes()
                print("")
                menu(username)
            elif user_input == "3":
                quit()
            else:
                print("press a number between 1-3")
        else:
            print("Enter only digits!")


# login_screen()

input("Press Any Key to continue...")

# while True:
#     k = readkey()
#     if k == "a":
#         print("pressed A")
#     if k == key.ENTER:
#         print("You pressed Enter")
#         break