class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_fave_movie(self, movie):
        self.favourites.append(movie)

    def remove_fave_movie(self, movie):
        self.favourites.remove(movie)

    def get_faves(self):
        fave_titles = []
        for favourite in self.favourites:
            fave_titles.append(favourite.title)
        return fave_titles