import requests

URL = "https://www.wikipedia.org/"

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    link_count = response.text.count('href')
    print(f"There are {link_count} links on the Wikipedia main page")
else:
    print(f"Unable to connect to {URL}", response.reason)
