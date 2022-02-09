class ExistingPlaylistName(Exception):
    def __init__(self):
        return "you already have a playlist with this name, please choose another name"


class ToManyPlaylistsForFreeEdition(Exception):
    def __init__(self):
        return "only premium helpers can create more than 5 playlists"


class ToManySongsInPlaylistForFreeEdition(Exception):
    def __init__(self):
        return "only premium helpers can add more than 20 songs into playlist"
