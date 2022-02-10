from core.user_interaction.app import App
from consolemenu import *
from consolemenu.items import *
from core.os_methods import is_user_valid
from core.helpers.user import User
from core.custom_exeptions.exeptions import ProblemLoggingIn


def login():
    _username = input("Enter ur user: ")
    _password = input("Enter ur password: ")
    _type = input("premium / free: ")
    _user = User(_username, _type, _password)
    if is_user_valid(_user):
        print("logged succesfuly")
        return _user
    else:
        raise ProblemLoggingIn


menu = ConsoleMenu("Welcome To Spotipy")
function_item = FunctionItem("Login", login)

menu.append_item(function_item)
menu.show()
