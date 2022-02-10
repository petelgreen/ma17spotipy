from core.os_methods import OSMethods
from core.models.Models import Consts
from core.helpers.user import User, UserType
from flask import Flask
from flask import Blueprint
import os


class App:
    def __init__(self, _user: User):
        self.user = _user
        o = OSMethods()
        self.artists = o.artists
        self.albums = o.albums
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
