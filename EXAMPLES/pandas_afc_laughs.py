import pandas as pd
import numpy as np

URL = "https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Laughs"

df_list = pd.read_html(URL)

movies  = df_list[1]
movies.columns = 'rank title director year'.split()
print(movies.head())
print('-' * 60)

def by_director(x):
    return [d.split()[::-1] for d in x]

movies_by_director = movies.value_counts("director").sort_index(key=by_director).sort_values(ascending=False, kind='stable')

for x, y in movies_by_director.items():
    print(x, y)
print('-' * 60)

movies_by_director = movies.groupby('director')
for director, movie_list in movies_by_director:
    print(director)
    for index, movie in movie_list[['title', 'year']].iterrows():
        print(f"   {movie.title} ({movie.year})")
print('-' * 60)
