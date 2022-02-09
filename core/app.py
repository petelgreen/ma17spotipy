from core.os_methods import OSMethods


class App:
    def __init__(self, path):
        o = OSMethods()
        o.load_files(path)
        self.artists = o.artists
        self.albums = o.albums

    def all_artists(self):
        return [artist.artist_name for artist in self.artists.values()]

    def artist_albums(self, artist_id):
        return [album.album_name for album in self.albums.values() if
                album.album_id in self.artists.get(artist_id).albums_ids]

    def all_songs(self):
        songs = []
        [[songs.append(song) for song in album.songs.values()] for album in [album for album in self.albums.values()]]
        return songs

    def top_ten_songs(self):
        return sorted(self.all_songs(), key=lambda x: x.popularity, reverse=True)[:10]

    def all_artist_songs(self, artist_id):
        songs = []
        [[songs.append(song) for song in album.songs.values()] for album in [album for album in self.albums.values() if
                album.album_id in self.artists.get(artist_id).albums_ids]]
        return songs

    def artist_top_ten_songs(self, artist_id):
        return sorted(self.all_artist_songs(artist_id), key=lambda x: x.popularity, reverse=True)[:10]

    def album_songs(self, album_id):
        return self.albums.get(album_id).songs



a = App(r"C:\Users\User\Desktop\petel\songs")
artist_id = "2l6M7GaS9x3rZOX6nDX3CM"
album_id = "5DvWThv9KXSsyZPDyozM49"
print(a.album_songs(album_id))
