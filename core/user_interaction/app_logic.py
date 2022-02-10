from core.os_methods import OSMethods
from core.models.Models import Consts, UserRank
from core.helpers.user import User, UserType


class App:
    def __init__(self, _user: User):
        self.user = _user
        o = OSMethods()
        self.artists = o.artists
        self.albums = o.albums
        self.audio_features = o.audio_features
        if self.is_user_artist():
            self.user.type = UserType.PREMIUM
        if self.user.type == UserType.FREE:
            self.results_num = Consts.FREE_RESULTS_NUM
        else:
            self.results_num = Consts.PREMIUM_RESULTS_NUM
        if self.user.type == UserType.FREE:
            self.top_results_num = Consts.FREE_RESULTS_NUM
        else:
            self.top_results_num = Consts.PREMIUM_USER_TOP_RESULTS

    def all_artists(self):
        return [artist.artist_name for artist in self.artists.values()][:self.results_num]

    def artist_albums(self, artist_id):
        return [album.album_name for album in self.albums.values() if
                album.album_id in self.artists.get(artist_id).albums_ids][:self.results_num]

    def all_songs(self):
        songs = []
        [[songs.append(song) for song in album.songs.values()] for album in [album for album in self.albums.values()]]
        return songs[:self.results_num]

    def top_ten_songs(self):
        return sorted(self.all_songs(), key=lambda x: x.popularity, reverse=True)[:self.top_results_num]

    def all_artist_songs(self, artist_id):
        songs = []
        [[songs.append(song) for song in album.songs.values()] for album in [album for album in self.albums.values() if
                                                                             album.album_id in self.artists.get(
                                                                                 artist_id).albums_ids]]
        return songs

    def artist_top_ten_songs(self, artist_id):
        return sorted(self.all_artist_songs(artist_id), key=lambda x: x.popularity, reverse=True)[:self.top_results_num]

    def album_songs(self, album_id):
        return {k: v for (k, v) in [x for x in self.albums.get(album_id).songs.items()][:self.results_num]}

    def is_user_artist(self):
        o = OSMethods()
        artists = o.artists
        artists_names = [artist.artist_name for artist in artists.values()]
        return self.user.username in artists_names

    # give user his audio_features_rank by his playlists
    def audio_features_rank(self):
        playlists = self.user.get_my_playlists()
        if playlists is None: return
        all_fav_songs = []
        for songs in playlists.values():
            for song in songs:
                all_fav_songs.append(song)
        print(all_fav_songs)
        rank_dict = {"danceability": 0, "energy": 0, "acousticness": 0, "valence": 0}
        for song_id in all_fav_songs:
            for feature, value in rank_dict.items():
                rank_dict[feature] += self.get_song_feature_rank(song_id, feature)
        songs_count = len(all_fav_songs)
        for feature, value in rank_dict.items():
            rank_dict[feature] = value / songs_count
        self.user.audio_features.energy = rank_dict.get("energy")
        self.user.audio_features.valence = rank_dict.get("valence")
        self.user.audio_features.danceability = rank_dict.get("danceability")
        self.user.audio_features.acousticness = rank_dict.get("acousticness")
        return rank_dict

    def get_song_feature_rank(self, song_id, feature):
        return int(self.audio_features.get(song_id).rank_dict.get(feature))

    def create_personal_custom_playlist(self):
        playlist = []
        rank_dict = self.audio_features_rank()
        for feature, value in rank_dict.items():
            feature_dict = self.get_songs_feature_rank(feature)
            res_song, res_val = min(feature_dict.items(), key=lambda x: abs(value - x[1]))
            playlist.append(res_song)
            feature_dict.pop(res_song)
            res_song2, res_val2 = min(feature_dict.items(), key=lambda x: abs(value - x[1]))
            playlist.append(res_song2)

        self.user.create_playlist("personal custom made playlist", playlist)
        return playlist

    def get_songs_feature_rank(self, feature):
        res_dict = {}
        for song_id, value in self.audio_features.items():
            res_dict[song_id] = value.get(feature)
        return res_dict

