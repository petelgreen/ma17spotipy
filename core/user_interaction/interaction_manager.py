from core.user_interaction.app_logic import App
from core.helpers.user import User
from flask import Flask
from core.os_methods import is_user_valid, create_user, get_user_type
from core.custom_exeptions.exeptions import ProblemLoggingIn
from consolemenu import *
from consolemenu.items import *
import logging
from core.models.Models import Consts

answer = input("1 - login\n"  "2 - sign up\n")
if str(answer) == "2":
    new_user = create_user()
    print(f"{new_user} created! try to log in now!")

_username = input("Enter ur user: ")
_password = input("Enter ur password: ")
_type = get_user_type(_username)
_user = User(_username, _type, _password)
if not is_user_valid(_user):
    raise ProblemLoggingIn

logic = App(_user)
logging.info(f"{_user} logged in")
_user = User("preen", "free", "123")

print("Please choose a way to interact with the app:\n")
interact = input("flask / console\n")
logging.basicConfig(filename=Consts.LOGS_PATTH, filemode='w', level=logging.INFO)

if interact == "flask":
    app = Flask(__name__)


    @app.route('/')
    def open_menu():
        return f"{_user} : logged succefully"


    @app.route('/artists', methods=['GET'])
    def all_artists():
        return str(logic.all_artists())


    @app.route('/albums/<_id>', methods=['GET'])
    def artist_albums(_id):
        return f" the albums of {_id}: {str(logic.artist_albums(_id))}"


    @app.route('/top/<_id>', methods=['GET'])
    def artist_top_ten_songs(_id):
        return f" top songs of {_id}: {str(logic.artist_top_ten_songs(_id))}"


    @app.route('/songs/<_id>')
    def album_songs(_id):
        return f" the songs of {_id} album: {str(logic.album_songs(_id))}"


    app.run(debug=True, use_reloader=False)


else:
    logging.info("using console menu")


    def all_artist_wrapper():
        print(logic.all_artists())


    def artist_albums_wrapper(_id):
        print(logic.artist_albums(_id))


    def artist_top_ten_songs_wrapper(_id):
        print(logic.artist_top_ten_songs(_id))


    def album_songs_wrapper(_id):
        print(logic.album_songs(_id))


    menu = ConsoleMenu(":)")
    menu.append_item(FunctionItem("get the artist", all_artist_wrapper))
    menu.append_item(FunctionItem("get artist albums by id", artist_albums_wrapper, ["66jtNcSqBSNontUk1Apdam"]))
    menu.append_item(
        FunctionItem("get artist top songs by id", artist_top_ten_songs_wrapper, ["66jtNcSqBSNontUk1Apdam"]))
    menu.append_item(FunctionItem("get the songs of an album", album_songs_wrapper, ["4OzXgERQxpLMFZpYrIDsHM"]))
    menu.append_item(FunctionItem("create playlist", _user.create_playlist, ["my cool playlist", [
        "\u05ea\u05d2\u05d9\u05d3\u05d5 \u05dc\u05d9 \u05d0\u05d7\u05e8\u05ea"]]))
    menu.append_item(FunctionItem("get ur playlists", _user.get_my_playlists))

    menu.start()
    menu.show()
