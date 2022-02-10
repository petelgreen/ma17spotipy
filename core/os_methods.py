import os, json
from core.models.Models import Album, Artist, Song, Consts
from core.custom_exeptions.exeptions import UserNotExist, NotCorrectPassword
import logging
from core.helpers.user import User


class OSMethods:
    def __init__(self):
        self.artists = {}
        self.albums = {}
        self.load_files()

    def load_files(self):
        [self.load_file(pos_json) for pos_json in os.listdir(Consts.SONGS_PATH) if pos_json.endswith('.json')]
        logging.info("loaded files succesfully")

    def load_file(self, file_name):
        file = open(Consts.SONGS_PATH + "/" + file_name)
        data = json.load(file).get('track')
        artists = data.get('artists')
        album = data.get('album')
        song_obj = Song(data.get('id'), data.get('name'), data.get('popularity'))
        album_obj = Album(album.get('id'), album.get('name'), artists)
        album_obj.add_song(song_obj)
        self.albums[album_obj.album_id] = album_obj
        for artist in artists:
            if artist.get('id') not in self.artists:
                self.artists[artist.get('id')] = Artist(artist.get('id'), artist.get('name'))
            self.artists[artist.get('id')].add_album(album_obj.album_id)


def is_user_valid(_user):
    file = open(Consts.USERS_PATH + "\\" + _user.username + ".json")
    user_data = json.load(file)
    file.close()
    if user_data is None:
        logging.error(f"{_user} (not exist user tried to log in)")
        raise UserNotExist
    if str(_user.password) == str(user_data.get("password")):
        return True
    logging.error(f"{_user} enter wrong password")
    raise NotCorrectPassword


def get_user_type(_username):
    file = open(Consts.USERS_PATH + "\\" + _username + ".json")
    user_data = json.load(file)
    file.close()
    return user_data.get("type")


def create_user():
    _username = input("new user: ")
    _password = input("new password: ")
    _type = input("premium / free: ")
    dict_to_save = {"password": _password, "type": _type}
    print(dict_to_save)
    file = open(Consts.USERS_PATH + "\\" + _username + ".json", "w")
    file.write(json.dumps(dict_to_save))
    logging.info(f"{_username} new user created")
    file.close()
    return User(_username, _type, _password)
