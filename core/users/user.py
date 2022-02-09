from core.custom_exeptions.exeptions import ExistingPlaylistName
import json


class User:
    def __init__(self, username):
        self.username = username

    def create_playlist(self, playlist_name, songs_list):
        user_playlists = self.read_playlists()
        if playlist_name in user_playlists:
            raise ExistingPlaylistName
        user_playlists[playlist_name] = songs_list
        self.save_playlist(user_playlists)

    def read_playlists(self):
        path = r"C:\Users\User\Desktop\petel\ma17spotipy\users/" + self.username
        file = open(path, "r")
        return json.load(file)

    def save_playlist(self, playlist):
        path = r"C:\Users\User\Desktop\petel\ma17spotipy\users/" + self.username
        file = open(path, "w")
        file.write(json.dumps(playlist))
        file.close()
