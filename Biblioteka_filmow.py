class Movie:
    def __init__(self, title, release, genre):
        self.title = title
        self. release = release
        self.genre = genre

        #Variable
        self._current_views=0

class Series(Movie):
    def __init__(self, title, release, genre, ep_no, season_no):
        super().__init__(title, release, genre)
        self.ep_no = ep_no
        self.season_no = season_no

         #Variable
        self._current_views = 0
