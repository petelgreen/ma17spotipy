from core.custom_exeptions.exeptions import ExistingPlaylistName, ToManySongsInPlaylistForFreeEdition, \
    ToManyPlaylistsForFreeEdition
from core.models.Models import UserType, Consts, UserRank
import json
import logging


class User:
    def __init__(self, username, type, password):
        self.username = username
        self.password = password
        self.type = type
        self.audio_features = UserRank()

    def create_playlist(self, playlist_name, songs_list):
        user_data = self.read_playlists()
        logging.info(f" {self.username} data: {user_data}")
        if user_data.get("playlists") is None:
            user_data["playlists"] = {}
            logging.info(f"{self.username} creating his first playlist")
        user_playlists = user_data.get("playlists")
        if self.type is UserType.FREE:
            if len(user_playlists) >= Consts.FREE_USER_PLAYLISTS_LIMIT:
                logging.error(f"{self.username} not premium user created too many playlists")
                raise ToManyPlaylistsForFreeEdition
            if len(songs_list) >= Consts.FREE_USER_SONGS_LIMIT:
                logging.error(f"{self.username} not premium user created added too many songs to playlist ")
                raise ToManySongsInPlaylistForFreeEdition
        if playlist_name in user_playlists:
            logging.error(f"{self.username} tried to create playlist which already exist")
            raise ExistingPlaylistName

        user_playlists[playlist_name] = songs_list
        user_data["playlists"] = user_playlists
        self.save_playlist(user_data)
        logging.info(f"{self.username} created playlist name: {playlist_name}")

    def read_playlists(self):
        path = Consts.USERS_PATH + '\\' + self.username + '.json'
        file = open(path, "r")
        return json.load(file)

    def save_playlist(self, playlist):
        path = Consts.USERS_PATH + '\\' + self.username + '.json'
        file = open(path, "w")
        file.write(json.dumps(playlist))
        logging.info(f"{self.username} playlists saved succesfully")
        file.close()

    def get_my_playlists(self):
        path = Consts.USERS_PATH + '\\' + self.username + '.json'
        file = open(path, "r")
        playlists = json.load(file).get("playlists")
        file.close()
        print(playlists)

    def __repr__(self):
        return f"{self.username} - {self.password} - {self.type}"
