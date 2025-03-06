class Movie:
    def __init__(self, title, release, genre):
        self.title = title
        self. release = release
        self.genre = genre

        #Variable
        self._current_views=0

    def __str__(self):
        return f"{self.title} ({self.release})"
    
    def play(self, viewed=1):
        self._current_views += viewed

    @property
    def current_views(self):
        return self._current_views
    
    @current_views.setter
    def current_views(self, value):
        if value >= self._current_views:
            self._current_views = value
        else:
            raise ValueError("Nie można zmniejszyć liczby wyświetleń")

class Series(Movie):
    def __init__(self, title, release, genre, ep_no, season_no):
        super().__init__(title, release, genre)
        self.ep_no = ep_no
        self.season_no = season_no

         #Variable
        self._current_views = 0
    
    def __str__(self):
        return f"{self.title} S{self.season_no:02d}E{self.ep_no:02d}"
    
