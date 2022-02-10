class Song:
    def __init__(self, song_id, song_name, popularity):
        self.song_id = song_id
        self.song_name = song_name
        self.popularity = popularity

    def __repr__(self):
        return f" Song: {self.song_name} - {self.popularity} "


class Album:
    def __init__(self, album_id, album_name, artists):
        self.album_id = album_id
        self.album_name = album_name
        self.artists = artists
        self.songs = {}

    def add_song(self, song: Song):
        self.songs[song.song_id] = song

    def __repr__(self):
        return f"{self.album_id}, {self.album_name}, {self.artists}, {self.songs}"


class Artist:
    def __init__(self, artist_id, artist_name):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.albums_ids = []

    def __repr__(self):
        return f" Artist :{self.artist_id}, {self.artist_name}, {self.albums_ids}"

    def add_album(self, album_id):
        self.albums_ids.append(album_id)


class SongRank:
    def __init__(self, dict_rank):
        self.dict_rank = dict_rank

    def __repr__(self):
        return f"{self.dict_rank}"


class UserRank:
    def __init__(self, danceability=0.5, energy=0.5, acousticness=0.5, instrumentalness='1.8e-06', valence=0.5):
        self.valence = valence
        self.danceability = danceability
        self.energy = energy
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness

    def __repr__(self):
        return f"{self.song_id}"


class UserType:
    FREE = "free"
    PREMIUM = "premium"


class Consts:
    FREE_USER_SONGS_LIMIT = 20
    FREE_USER_PLAYLISTS_LIMIT = 5
    SONGS_PATH = r"C:\Users\User\Desktop\petel\songs"
    PREMIUM_RESULTS_NUM = 10000000
    FREE_RESULTS_NUM = 5
    FREE_USER_TOP_RESULTS = 5
    PREMIUM_USER_TOP_RESULTS = 10
    USERS_PATH = r"C:\Users\User\Desktop\petel\ma17spotipy\users"
    LOGS_PATTH = r"C:\Users\User\Desktop\petel\ma17spotipy\logs.log"
    AUDIO_FEATURES_PATH = r"C:\Users\User\Desktop\petel\audio_features"
