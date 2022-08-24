import login


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


def main():
    """
    Runs the programs functions.
    """
    welcome()
    login.check_if_exists()
    test = login.success_login()
    print(test)


# def welcome_user(username):
#     """
#     Welcomes you to the game
#     """
#     message = """
#     Welcome
#     """
#     print(message)
#     print(username)


main()
