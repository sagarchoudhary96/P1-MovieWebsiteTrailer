#!/usr/bin/python
# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
import requests

# base url's
youtube_base_url = "https://www.youtube.com/watch?v="
poster_base_url = "https://image.tmdb.org/t/p/w780"
video_base_url = "https://api.themoviedb.org/3/movie/"

# api_credentials
params = {'api_key': 'YOUR_API_KEY_HERE'}

# request for movies
response = requests.get('https://api.themoviedb.org/3/movie/upcoming', params = params).json()

# to store movies details
movies = []

for i in xrange(6):
    movie_res = response['results'][i]
    movie_title = movie_res['title']
    movie_poster = poster_base_url + movie_res['poster_path']
    if movie_res['vote_average'] > 2:
        movie_rating = "&#9733 "*int(movie_res['vote_average']/2)
    else:
        movie_rating = "&#9733 &#9733"
    movie_video_response = requests.get(video_base_url + str(movie_res['id']) + "/videos", params = params).json()
    movie_video_url = youtube_base_url + movie_video_response['results'][0]['key']
    movie = media.Movie(movie_title, movie_rating, movie_poster, movie_video_url)
    movies.append(movie)
    i+=1

# open pages
fresh_tomatoes.open_movies_page(movies)
