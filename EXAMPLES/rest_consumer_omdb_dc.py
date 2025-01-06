import requests
from pprint import pprint
from dataclasses import make_dataclass

with open('omdbapikey.txt') as api_in:
    OMDB_API_KEY = api_in.read().rstrip()

OMDB_URL = "http://www.omdbapi.com"

MOVIE_TITLES = [
    'Black Panther',
    'Frozen',
    'Top Gun: Maverick',
    'Bullet Train',
    'Death on the Nile',
    'Casablanca',
    'The Producers',
    'Buckaroo Banzai',
    'Deadpool and Wolverine',
]

def main():
    with requests.Session() as session:
        session.params.update({"apikey": OMDB_API_KEY})
        movies = []
        for movie_title in MOVIE_TITLES:
            params = {'t': movie_title}
            response = session.get(OMDB_URL, params=params)
            if response.status_code == requests.codes.OK:
                raw_data = response.json()
                keys = raw_data.keys()
                Movie = make_dataclass("movie", keys)
                m = Movie(*raw_data.values())
                movies.append(m)
    for movie in sorted(movies, key=lambda m: m.Year):
        print(movie.Year, movie.Title)

if __name__ == '__main__':
    main()
