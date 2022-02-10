from core.user_interaction.app import App
from core.helpers.user import User
from flask import Flask
from core.os_methods import is_user_valid
from core.custom_exeptions.exeptions import ProblemLoggingIn
from consolemenu import *
from consolemenu.items import *

# _username = input("Enter ur user: ")
# _password = input("Enter ur password: ")
# _type = input("premium / free: ")
# _user = User(_username, _type, _password)
# if not is_user_valid(_user):
#     raise ProblemLoggingIn
# logic = App(_user)
_user = User("preen", "free", "123")
logic = App(_user)

print("Please choose a way to interact with the app:\n")
interact = input("flask / console\n")
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


    app.run(debug=True)
else:
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

    menu.start()
    menu.show()
