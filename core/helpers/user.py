from core.custom_exeptions.exeptions import ExistingPlaylistName, ToManySongsInPlaylistForFreeEdition, \
    ToManyPlaylistsForFreeEdition
from core.models.Models import UserType, Consts
from core.os_methods import OSMethods
import json


class User:
    def __init__(self, username, type, password):
        self.username = username
        self.password = password
        self.type = type
        if self.is_user_artist(): self.type = UserType.PREMIUM

    def create_playlist(self, playlist_name, songs_list):
        user_playlists = self.read_playlists()
        if self.type is UserType.FREE:
            if len(user_playlists) >= Consts.FREE_USER_PLAYLISTS_LIMIT:
                raise ToManyPlaylistsForFreeEdition
            if len(songs_list) >= Consts.FREE_USER_SONGS_LIMIT:
                raise ToManySongsInPlaylistForFreeEdition

        if playlist_name in user_playlists:
            raise ExistingPlaylistName
        user_playlists[playlist_name] = songs_list
        self.save_playlist(user_playlists)

    def read_playlists(self):
        path = Consts.USERS_PATH + self.username
        file = open(path, "r")
        return json.load(file)

    def save_playlist(self, playlist):
        path = Consts.USERS_PATH + self.username
        file = open(path, "w")
        file.write(json.dumps(playlist))
        file.close()

    def is_user_artist(self):
        artists = OSMethods().artists
        artists_names = [artist.artist_name for artist in artists.values()]
        return self.username in artists_names

    def __repr__(self):
        return f"{self.username} - {self.password} - {self.type}"


