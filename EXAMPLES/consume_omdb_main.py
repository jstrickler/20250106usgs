import asyncio
import time

from nfrtitles import get_nfr_title_list
import consume_omdb_threads
import consume_omdb_procs
import consume_omdb_cf_threads
import consume_omdb_cf_procs
import consume_omdb_async
import consume_omdb_serial

MODULES = (
    consume_omdb_threads,
    consume_omdb_procs,
    consume_omdb_cf_threads,
    consume_omdb_cf_procs,
    consume_omdb_async,
    consume_omdb_serial,
)


def main():

    movie_titles: list[str] = get_nfr_title_list()

    with open('omdbapikey.txt') as api_in:
        omdb_api_key = api_in.read().rstrip()

    for module in MODULES:
        print(f"{module.__name__:25s}", end=" ")
        start_time = time.perf_counter()
        if module.__name__ == 'consume_omdb_async':
            ratings = asyncio.run(module.get_ratings(movie_titles, omdb_api_key))
        else:
            ratings = module.get_ratings(movie_titles, omdb_api_key)
        total_time = time.perf_counter() - start_time

        print(f"length: {len(ratings)} total time: {total_time:6.2f}")

if __name__ == '__main__':
    main()
