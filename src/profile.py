class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_fave_movie(self, movie):
        self.favourites.append(movie.title)

    def remove_fave_movie(self, movie):
        self.favourites.remove(movie)

    def get_faves(self):
        return self.favourites
