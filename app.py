from flask import Flask, render_template, request, url_for
import requests
import os
import urllib.request as ur
import json
import json

app = Flask(__name__)


# represents home page
@app.route('/')
def index():

    results = home_random()
    list_of_gifs = results['results']

    # points to index.html page
    return render_template('index.html', list_of_gifs=list_of_gifs)


@app.route('/search')
def make_gif():

    search_term = request.args.get('gifs')

    response = requests.get(
        f'https://api.tenor.com/v1/search?q={search_term}&key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(response.content)
        # print(top_10gifs['results'])
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None


''' presets sports as the search term so users see sports when routed to sports change '''
@app.route('/sports')
def sports():
    search_term = "sports"
    response = requests.get(
        f'https://api.tenor.com/v1/random?q={search_term}&?key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        top_10gifs = json.loads(response.content)
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None


@app.route('/entertainment')
def entertainment():

    search_term = "entertainment"
    response = requests.get(
        f'https://api.tenor.com/v1/random?q={search_term}&?key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        top_10gifs = json.loads(response.content)
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None


@app.route('/coding')
def coding():

    search_term = "coding"
    response = requests.get(
        f'https://api.tenor.com/v1/random?q={search_term}&?key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        top_10gifs = json.loads(response.content)
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None


@app.route('/trending')
def popular():

    search_term = "trending"
    response = requests.get(
        f'https://api.tenor.com/v1/trending?key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        top_10gifs = json.loads(response.content)
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None


''' Uses random gifs API to display randomized gifs on the homepage'''


def home_random():
    response = requests.get(
        "https://api.tenor.com/v1/random?q=random&?key=1F2TY5LFTDOH&limit=10")

    if response.status_code == 200:
        random_gifs = json.loads(response.content)
    else:
        random_gifs = None

    return random_gifs


if __name__ == "__main__":
    app.run(debug=True, port=8080)
