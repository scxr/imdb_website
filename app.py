from imdb import IMDb
from flask import Flask, render_template, request
from modules.get_movie import find_movie
from modules.get_top import get_top
from modules.get_bottom import get_bottom
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/searchmovie', methods=['POST'])
def get_movie_details():
    movie = request.form['movie']
    actors, genre, director, plot,title, image, rating,date, length = find_movie(movie)
    return render_template('movie_details.html', 
                            actors=actors, 
                            genre=genre, 
                            director=director, 
                            plot=plot, 
                            title=title, 
                            image_sent=image, 
                            rating=rating,
                            released=date,
                            length=length)

@app.route('/bottom100')
def bottom_100():
    bottom = get_bottom()
    return render_template('bottom100.html', movies=bottom)

@app.route('/top100')
def top_250():
    top = get_top()
    return render_template('top250.html', movies=top)

@app.route('/fromlisting/<movie>')
def get_movie_details_from_250(movie):
    actors, genre, director, plot,title, image, rating,date, length = find_movie(movie)
    return render_template('movie_details.html', 
                            actors=actors, 
                            genre=genre, 
                            director=director, 
                            plot=plot, 
                            title=title, 
                            image_sent=image, 
                            rating=rating,
                            released=date,
                            length=length)

if __name__ == "__main__":
    app.run(debug=True)