from imdb import IMDb
ia = IMDb()
def find_movie(title):  
    movies = ia.search_movie(title)
    movie = ia.get_movie(movies[0].movieID)
    title = movie
    image = movie.data['cover url']
    genre = movie['genres'][0]
    release = movie['year']
    length = movie['runtimes'][0]
    rating = movie['rating']
    plot = movie['plot'][0].split('::')[0]
    actors = []
    try:
        director = movie['directors'][0]['name']
    except Exception:
        director = 'Not Found'
    for i in range(3):
        actors.append(movie['actors'][i]['name'])
    return actors, genre, director, plot, title, image, rating, release, length