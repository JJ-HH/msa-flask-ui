from flask import Flask, render_template
import requests


app = Flask(__name__)
api_endpoint = "http://flask-rest.default.svc.cluster.local:5000/ns_movies/"

@app.route("/", methods=['GET'])
def render_home_page():
    all_movies = requests.get(api_endpoint).json()
    return render_template('home.html', movies=all_movies, **all_movies)

@app.route("/detail/<movie_id>", methods=['GET'])
def render_detail_page(movie_id):
    movie = requests.get(f'{api_endpoint}{movie_id}').json()
    return render_template('detail.html', movie=movie)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
