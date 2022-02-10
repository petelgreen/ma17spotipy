from tokenize import String
import requests
from flask import Flask, request
from core.helpers.user import User, UserType
from core.user_interaction.app import App
from app import App
from core.user_interaction.console_menu import login

_user = login()
app = Flask(__name__)


@app.route('/')
def open_menu():
    return f"{_user} : logged succefully"


@app.route('/artists', methods=['GET'])
def all_artists():
    a = App(_user)
    return str(a.all_artists())


@app.route('/albums/<_id>', methods=['GET'])
def artist_albums(_id):
    a = App(_user)
    return f" the albums of {_id}: {str(a.artist_albums(_id))}"


@app.route('/top/<_id>', methods=['GET'])
def artist_top_ten_songs(_id):
    a = App(_user)
    return f" top songs of {_id}: {str(a.artist_top_ten_songs(_id))}"


@app.route('/songs/<_id>')
def album_songs(_id):
    a = App(_user)
    return f" the songs of {_id} album: {str(a.album_songs(_id))}"


def main():
    #app.run(debug=True)


if __name__ == '__main__':
    main()
