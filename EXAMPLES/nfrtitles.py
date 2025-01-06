import requests
from bs4 import BeautifulSoup

URL = "https://www.loc.gov/programs/national-film-preservation-board/film-registry/complete-national-film-registry-listing/"


def get_nfr_title_list() -> list[str]:
    response = requests.get(URL)
    if response.status_code == requests.codes.OK:
        movies: list[str] = []
        soup = BeautifulSoup(response.text, "lxml")
        for movie in soup.findAll('th', scope="row"):
            movies.append(movie.text)
        return movies
    else:
        raise Exception("Unable to retrieve movie titles")

if __name__ == '__main__':
    movies = get_nfr_title_list()
    print(f"{len(movies)} movies added")
    print(movies[:20])
