import requests
import random
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")


def get_genre_id(genre_name):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    genres = response.json().get("genres", [])
    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None


def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    movies = response.json().get("results", [])
    return movies


def recommend_movie(genre_name):
    genre_id = get_genre_id(genre_name)
    if not genre_id:
        return f"Genre '{genre_name}' not found."

    movies = get_movies_by_genre(genre_id)
    if not movies:
        return f"No movies found for genre '{genre_name}'."

    movie = random.choice(movies)
    return f"Recommended Movie: {movie['title']} (Rating: {movie['vote_average']})"


if __name__ == "__main__":
    genre_name = input("Enter a movie genre: ")
    recommendation = recommend_movie(genre_name)
    print(recommendation)
