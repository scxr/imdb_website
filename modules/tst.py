from imdb import IMDb
from pprint import pprint
ia = IMDb()

def tst(mv):
    movies = ia.search_movie(mv)
    movie = ia.get_movie(movies[0].movieID)
    print(movie.data['cover url'])
    
tst('requiem for a dream')