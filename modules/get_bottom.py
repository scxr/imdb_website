from imdb import IMDb
ia = IMDb()
def get_bottom():
    return ia.get_bottom100_movies()