class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
sara_smile = Song("Sara Smile", "Hall and Oates", "Pop")

                
    
