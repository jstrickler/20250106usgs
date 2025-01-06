import time
from multiprocessing.dummy import Pool
from functools import partial

from omdblib import OMDB


def get_rt_score(omdb, title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score


def get_ratings(movie_titles, omdb_api_key):
    omdb = OMDB(omdb_api_key)
    get_score = partial(get_rt_score, omdb)
    thread_pool = Pool(16)
    ratings = thread_pool.map(get_score, movie_titles)
    return ratings


if __name__ == '__main__':
    from nfrtitles import get_nfr_title_list
    movies = get_nfr_title_list()
    # movies = ["Star Wars", "Return of the Jedi", "The Empire Strikes Back"]
    with open('omdbapikey.txt') as omdb_api_in:
        api_key = omdb_api_in.read().rstrip()

    ratings = get_ratings(movies, api_key)
    print(f"ratings: {ratings}")

