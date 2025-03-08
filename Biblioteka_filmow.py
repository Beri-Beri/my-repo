import random
import datetime

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
    
library = []

def add_to_library(item):
    if isinstance(item, (Movie, Series)):
        library.append(item)
    else:
        print("Element, który chcesz dodać nie jest filmem lub serialem")

def generate_library():
    #movies_ex
    add_to_library(Movie("Inception", 2010, "Sci-Fi"))
    add_to_library(Movie("The Matrix", 1999, "Sci-Fi"))
    add_to_library(Movie("Avatar", 2009, "Sci-Fi"))
    #series_ex
    add_to_library(Series("Breaking Bad", 2008, "Drama", 1, 1))
    add_to_library(Series("Breaking Bad", 2008, "Drama", 2, 1))
    add_to_library(Series("Stranger Things", 2016, "Horror", 1, 1))
    add_to_library(Series("Stranger Things", 2016, "Horror", 2, 1))

def get_movies():
    return [item for item in library if isinstance(item, Movie) and not isinstance(item, Series)]

def get_series():
    return [item for item in library if isinstance(item, Series)]

def search(title): 
    search_result = [item for item in library if title.lower() in item.title.lower()]
    return sorted(search_result, key=lambda result: result.title)

def generate_views():
    if library:
        item = random.choice(library)
        item.play(random.randint(1, 100))
        return item
    return None

def run_views(n=10):
    for i in range(n):
        generate_views()

def top_titles(content_type, top_n=3):
    if content_type == "movie":
        filtered = get_movies()
    elif content_type == "series":
        filtered = get_series()
    else:
        filtered = library
    return sorted(filtered, key=lambda top: top.current_views, reverse=True)[:top_n]

def add_seasons(title, release, genre, season_no, add_ep):
    for ep_no in range(1, add_ep + 1):
        add_to_library(Series(title, release, genre, season_no, ep_no))

def count_ep(series_title):
    return sum(1 for item in library if isinstance(item, Series) and item.title.lower() == series_title.lower())
