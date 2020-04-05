from imdb import IMDb
ia = IMDb()
def get_top():
    return ia.get_top250_movies()[0:100]
get_top()