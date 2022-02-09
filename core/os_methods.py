import os, json
from core.models.Models import Album, Artist, Song, Consts


class OSMethods:
    def __init__(self):
        self.artists = {}
        self.albums = {}
        self.load_files()

    def load_files(self):
        [self.load_file(pos_json) for pos_json in os.listdir(Consts.SONGS_PATH) if pos_json.endswith('.json')]

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

