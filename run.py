""" Math Daily """
from random import randint
from datetime import date
import os
from readchar import readkey, key
from termcolor import colored, cprint
import scope


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


def create_chunk_list(my_list, chunk_size):
    """ Creates smaller chunks of list """
    # Splits the list into indivdual pieces
    split_list = my_list.split()

    for i in range(0, len(split_list), chunk_size):
        yield split_list[i:i + chunk_size]

# -------- ___________ ----------


def loading():
    """ Shows a loading text, so the user knows its working """
    new_line()
    center_text_color("Loading...", "green", "bold")


def center_text(message):
    """
    Center the text
    example:
    center_text("Hello, world!")
    """
    print(message.center(80))


def center_text_color(message, color, attr):
    """
    Center the text with color and attr
    example:
    center_text_color("Hello, world!", "magenta", "bold")
    """
    text = colored(message, color, attrs=[attr])
    cprint(text.center(92))


def space_top():
    """ Creates 5 break lines when called """
    for unused in range(5):
        print("")


def new_line():
    """ Creates 1 new line when called """
    print("")


def input_message():
    """ Enter here string """
    return "                           Enter here: "


def new_screen():
    """ Starts new screen """
    clear_screen()
    space_top()


def welcome_message():
    """
    Welcomes you to the game
    """
    new_screen()
    center_text_color("Welcome player", "green", "bold")
    center_text("Please login and enjoy your daily math.")


def ask_new_user():
    """ Ask if you are a new user """
    new_user = True
    while True:
        new_line()
        center_text_color("Are you a new user?", "green", "bold")
        center_text("Y or N")
        k = readkey()
        if k == "y":
            loading()
            check_if_exists(new_user)
        elif k == "n":
            new_user = False
            check_if_exists(new_user)
        elif k != "y":
            new_screen()
            center_text_color("Press Y for yes and N for no",
                              "yellow", "bold")


def create_username():
    """ Creates new user name """
    while True:
        new_screen()
        center_text_color("To go back, just press Enter when its empty.",
                          "yellow", "bold")
        new_line()
        center_text_color("Please enter your name.", "green", "bold")
        # Strip takes away the spaces when writing the name
        username = input(input_message()).strip()
        if len(username) == 0:
            login_screen()
        # Asks if there is alphanumeric chararacters only
        if username.isalnum():
            if len(username) > 15:
                new_screen()
                center_text_color("To many characters!", "yellow", "bold")
                center_text("Please limit yourself to 15.")
                new_line()
                press_any_key()
            else:
                loading()
                return username.lower()
        new_screen()
        center_text("Please try again")
        center_text_color("Only alphabetic and numeric characters.",
                          "yellow", "bold")
        new_line()
        press_any_key()


def create_user_pin():
    """ Creates new user pin code """
    new_screen()
    center_text_color("Please enter a 4 digit pin code", "green", "bold")
    while True:
        try:
            user_pin = int(input(input_message()))
            test_pin_lenght = len(str(user_pin))
            if test_pin_lenght == 4:
                loading()
                return user_pin
            else:
                raise ValueError
        except ValueError:
            loading()
            new_screen()
            center_text_color("That's not a valid option!",
                              "red", "bold")
            center_text_color("Use 4 digits to create a pin code",
                              "yellow", "bold")


def create_birth_year():
    """ Creates new user age """
    new_screen()
    center_text_color("Please enter a 4 digit year of birth",
                      "green", "bold")
    while True:
        try:
            birth_year = int(input(input_message()))
            test_pin_lenght = len(str(birth_year))
            if test_pin_lenght == 4:
                loading()
                return birth_year
            else:
                raise ValueError
        except ValueError:
            clear_screen()
            space_top()
            center_text_color("That's not a valid option!",
                              "red", "bold")
            center_text_color("Use 4 digits to create year of birth",
                              "yellow", "bold")


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

    def user_cell(new_user):
        """
        If user_cell is none, checks if new_user is true else it
        will tell you the account doesn't exist and gives you a choice
        to try again.

        If user_cell is not none, checks if new_user is true and return
        else it will tell you that account doesn't exist and promts
        you to try again.
        """
        while True:
            # Defines the username from the function
            username = create_username()
            # Checks the users wks for the username
            user_cell = users_wks.find(username, in_column=1)
            # If it doesn't exist
            if user_cell is not None:
                if new_user is True:
                    clear_screen()
                    new_screen()
                    center_text_color("This exists already, try another.",
                                      "red", "bold")
                    new_line()
                    press_any_key()
                    clear_screen()
                else:
                    return [username, user_cell]
            # If it does exist
            else:
                # Asks if the user name exists and new_user is True or False
                if user_cell is None:
                    if new_user is True:
                        return [username, user_cell]
                    else:
                        new_line()
                        new_screen()
                        center_text_color("This account don't exist",
                                          "red", "bold")
                        while True:
                            center_text("Try again? Y or N")
                            k = readkey()
                            if k == "y":
                                loading()
                                check_if_exists(False)
                                break
                            elif k == "n":
                                loading()
                                login_screen()
                                break
                            elif k != "y":
                                space_top()
                                message = ("Press Y for yes and N for no")
                                center_text_color(message, "yellow", "bold")
                else:
                    return [username, user_cell]

    value = user_cell(new_user)
    username = value[0]
    user_cell = value[1]
    user = make_capitalize(username)
    num_tries = 0
    while True:
        user_pin = create_user_pin()
        # If username exist do this:
        if user_cell is not None:
            # Access the pin code from google sheet with usernames
            pin_code = int(users_wks.cell(user_cell.row, 2).value)
            # Checks the pincode
            if pin_code == user_pin:
                success_login(username)
            if pin_code != user_pin:
                num_tries += 1
                if num_tries == 3:
                    while True:
                        new_line()
                        clear_screen()
                        new_screen()
                        center_text_color("You tried 3 times, are you "
                                          + user + "?", "yellow", "bold")
                        center_text("Try again? Y or N")
                        k = readkey()
                        if k == "y":
                            num_tries = 0
                            break
                        if k == "n":
                            loading()
                            login_screen()
                        if k != "y":
                            new_screen()
                            center_text("Press Y for yes and N for no")
                else:
                    clear_screen()
                    new_screen()
                    center_text(str(num_tries) + " of 3 tries!")
                    center_text_color("Wrong pin code, try again!",
                                      "red", "bold")
                    new_line()
                    press_any_key()
        # If username don't exist do this
        else:
            loading()
            birth_year = create_birth_year()
            update_users_worksheet(username, user_pin,
                                   birth_year, date_today())
            reset_treats(username)
            new_screen()
            center_text_color("Your account is setup", "green", "bold")
            center_text_color("Please proceed to login", "green", "bold")
            new_line()
            press_any_key()
            check_if_exists(False)


def press_any_key():
    """ Press any key to continue """
    center_text_color("Press any key to continue...",
                      "magenta", "bold")
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
    user = make_capitalize(username)
    center_text_color("Welcome to Daily Math " + user, "green", "bold")
    center_text("May your calculations be true!")
    center_text("Todays date is: " + date_today())
    new_line()
    press_any_key()
    loading()
    random_qoutes()
    new_line()
    press_any_key()
    loading()


def latest_login(username):
    """
    Checks if the latest date you logged in match todays, and if
    not it changes it to today.
    """
    # Finds the users row
    row_select = find_user(username)
    # checks the value of date in google sheets
    users_latest_login = users_wks.cell(row_select, 4).value
    # Checks the value of the treats
    today_user_treats = users_wks.cell(row_select, 5).value
    total_user_treats = users_wks.cell(row_select, 6).value
    user = make_capitalize(username)
    if date_today() == users_latest_login:
        new_screen()
        if int(today_user_treats) > 5:
            center_text_color("Great job " + user, "green", "bold")
            center_text("You are done for today, but feel free to continue!")
        new_line()
        center_text("Todays earned treats: "
                    + str(today_user_treats) + " out of 5")
        center_text_color("This is your total amount of treats earned: "
                          + str(total_user_treats), "cyan", "bold")
        new_line()
        press_any_key()
        menu(username)
    else:
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


def display_chunk_list(chunk_list):
    """
    Goes through the list and center_text() it to look nice.
    """
    for unused, value in enumerate(chunk_list):
        center_text(" ".join(value))


def random_qoutes():
    """
    Gives you an random qoute from google sheets
    """
    new_screen()
    # Gets the lenght of qoutes and gives a random number
    length = quotes_wks.row_count
    random_number = randint(2, length)
    # Gets the Qoute from Google sheet
    qoutes = quotes_wks.cell(random_number, 1).value
    # Creates a new list and prints it out
    chunk_list = list(create_chunk_list(qoutes, 8))
    display_chunk_list(chunk_list)
    # Gets the Author from Google sheet
    author = quotes_wks.cell(random_number, 2).value
    center_text_color("- " + author, "cyan", "bold")


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
    new_line()
    user = make_capitalize(username)
    loading()
    new_screen()
    message = "you now have three choices of difficulty"
    center_text_color(f"{user}, {message}", "green", "bold")
    center_text("1. Age 3-5")
    center_text(" 2. Age 6-12")
    center_text("3. Age 12+")
    center_text("4. Go back to menu")


def random_questions(num):
    """
    Random question
    """
    # Gets the num and selects the appropiet worksheet
    if num == 1:
        worksheet = questions_1_wks
    elif num == 2:
        worksheet = questions_2_wks
    elif num == 3:
        worksheet = questions_3_wks
    new_line()
    # Gets the amount of rows
    length = worksheet.row_count
    # Creates a random number
    random_number = randint(2, length)
    # Selects a random question and the corresponing answer
    question = worksheet.cell(random_number, 1).value
    answer = worksheet.cell(random_number, 2).value
    return [question, answer]


def answer_question(username, num):
    """
    Here you will get to answer the question given to you.
    """
    loading()
    new_screen()
    center_text_color("To go back, just press Enter when its empty.",
                      "yellow", "bold")
    question_list = random_questions(num)
    user = make_capitalize(username)
    tries = 0
    while True:
        # Creates smaller chunks, so the center text can work is magic
        chunk_list = list(create_chunk_list(question_list[0], 12))
        display_chunk_list(chunk_list)
        while True:
            new_line()
            # Strip away the spaces from user input
            user_input = input(input_message()).strip()
            if len(user_input) == 0:
                menu(username)
            if user_input.find(".") > 0:
                message = "Your answer contains a dot, please use commas."
                new_line()
                center_text_color(message, "yellow", "bold")
                press_any_key()
                break
            else:
                break
        if user_input == question_list[1]:
            new_screen()
            earn_treats(username)
            new_screen()
            message = "That is correct " + str(user) + ", good work!"
            center_text_color(message, "green", "bold")
            center_text("Here is a treat for you!")
            new_line()
            center_text("????")
            # Finds the users row
            row_select = find_user(username)
            # checks the value of date in google sheets
            today_user_treats = users_wks.cell(row_select, 5).value
            total_user_treats = users_wks.cell(row_select, 6).value
            user = make_capitalize(username)
            if int(today_user_treats) >= 5:
                new_line()
                center_text_color("Great job " + user, "green", "bold")
                done = "You are done for today, but feel free to continue!"
                center_text(done)
            new_line()
            center_text_color("Todays earned treats: "
                              + str(today_user_treats) + " out of 5",
                              "cyan", "bold")
            center_text("This is your total amount of treats earned: "
                        + str(total_user_treats))
            another_question(username, num)
            break
        else:
            tries += 1
            if tries == 3:
                while True:
                    while True:
                        new_screen()
                        center_text("Press 1 for solution.")
                        center_text("Press 2 for to keep trying.")
                        center_text("Press 3 to go back to menu")
                        k = readkey()
                        if k == "1":
                            new_screen()
                            # Creates smaller chunks
                            chunk_list = list(create_chunk_list
                                              (question_list[0], 12))
                            display_chunk_list(chunk_list)
                            new_line()
                            center_text(f"The answer is {question_list[1]}")
                            another_question(username, num)
                        elif k == "2":
                            loading()
                            answer_question(username, num)
                        elif k == "3":
                            loading()
                            menu(username)
                        else:
                            text = "Did not press 1, 2 or 3... Try again"
                            new_line()
                            center_text_color(text, "yellow", "bold")
                            press_any_key()
            new_screen()
            center_text_color("Wrong answer, keep trying " + user + "!",
                              "red", "bold")
            center_text(str(tries) + " out of 3")
            center_text("After 3 tries, a choice will be given.")
            new_line()
            press_any_key()


def another_question(username, num):
    """
    Asks if you want another question in the same difficulty
    """
    while True:
        new_line()
        center_text_color("Do you want to continue?",
                          "green", "bold")
        center_text("Press Y for yes and N for no")
        k = readkey()
        if k == "y":
            loading()
            answer_question(username, num)
            break
        if k == "n":
            loading()
            menu(username)
            break
        if k != "y":
            new_screen()
            new_line()
            center_text_color("Press Y for yes and N for no",
                              "yellow", "bold")
            press_any_key()
            new_screen()


def make_capitalize(username):
    """
    Makes the username uppercase for readability.
    """
    return username.capitalize()


def check_your_age(username, your_age, age, user, num):
    """
    Check if you want to play, though your age is
    above the recommended age.
    """
    def if_your_age():
        """ Creates smaller code, for more readability """
        new_screen()
        message = "Your age is not recommended for this difficulty, "
        center_text_color(message + user + ".", "red", "bold")
        center_text("Do you want to continue?")
        center_text("Press Y for yes and N for no")
        while True:
            k = readkey()
            if k == "y":
                clear_screen()
                loading()
                answer_question(username, num)
                break
            if k == "n":
                loading()
                choose_difficulty(username)
                break
            if k != "y":
                loading()
                if_your_age()
    if age == 13:
        clear_screen()
        loading()
        answer_question(username, num)
    else:
        if your_age > age:
            loading()
            if_your_age()


def choose_difficulty(username):
    """
    Here you get a choice to choose your difficulty level
        - Age 3-5
        - Age 6-12
        - Age 12+
        - Menu
    """
    new_screen()
    your_age = calculate_age(username)
    instructions(username)
    user = make_capitalize(username)
    while True:
        k = readkey()
        if k == "1":
            age = 5
            num = 1
            loading()
            check_your_age(username, your_age, age, user, num)
            break
        elif k == "2":
            age = 12
            num = 2
            loading()
            check_your_age(username, your_age, age, user, num)
            break
        elif k == "3":
            age = 13
            num = 3
            loading()
            check_your_age(username, your_age, age, user, num)
            break
        elif k == "4":
            loading()
            menu(username)
        elif k != "y":
            clear_screen()
            space_top()
            message = "It's not that hard "
            center_text_color(message + user + "...",
                              "yellow", "bold")
            center_text("Pick a number between 1 and 4!")
            press_any_key()
            instructions(username)


def earn_treats(username):
    """
    Give the user treats for each completed question.
    """
    loading()
    # Finds the users row
    row_select = find_user(username)
    # checks the value of treats in google sheets
    user_treats = users_wks.cell(row_select, 5).value
    total_user_treats = users_wks.cell(row_select, 6).value
    # Sets the users_treats to be int and adds more readability
    increase_treats = int(user_treats)
    total_increase_treats = int(total_user_treats)
    # Access the users worksheets and increases the treats by 1
    users_wks.update_cell(row_select, 5, increase_treats+1)
    users_wks.update_cell(row_select, 6, total_increase_treats+1)


def reset_treats(username):
    """
    Resets the users treats for a new day.
    """
    loading()
    # Finds the users row
    row_select = find_user(username)
    # Access the users worksheets and sets the treats back to 0
    users_wks.update_cell(row_select, 5, 0)
    # Checks if users got total users treats
    total_user_treats = users_wks.cell(row_select, 6).value
    if total_user_treats is None:
        users_wks.update_cell(row_select, 6, int(0))


def login_screen():
    """
    First thing you see and that you need to login / register to move on.
    """
    loading()
    welcome_message()
    ask_new_user()


def menu(username):
    """
    This is where you return to when your done with certain things
    """
    new_screen()
    while True:
        center_text_color("Menu, press the number to continue",
                          "green", "bold")
        center_text("1. Question")
        center_text("2. Motivational quote")
        center_text("3. Check my treats")
        center_text("4. Quit")
        k = readkey()
        if k == "1":
            loading()
            choose_difficulty(username)
        elif k == "2":
            new_screen()
            loading()
            random_qoutes()
            new_line()
            press_any_key()
            loading()
            menu(username)
        elif k == "3":
            loading()
            latest_login(username)
        elif k == "4":
            new_line()
            center_text("Are you sure? Y or N")
            while True:
                k = readkey()
                if k == "y":
                    loading()
                    clear_screen()
                    new_screen()
                    message = "You have succesfully quit, see you next time!"
                    center_text_color(message, "green", "bold")
                    quit()
                elif k == "n":
                    loading()
                    menu(username)
                elif k != "y":
                    loading()
                    new_screen()
                    center_text_color("You are about to quit", "red", "bold")
                    center_text("Press Y for yes and N for no")
        else:
            new_line()
            center_text_color("Did not press 1, 2 or 3.. Try again",
                              "yellow", "bold")
            press_any_key()
            new_screen()


login_screen()
