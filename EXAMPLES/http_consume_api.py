import sys
import requests
from pprint import pprint

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

with open('dictionaryapikey.txt') as api_key_in:
    API_KEY = api_key_in.read().rstrip()  # get credentials

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},
        # ssl, proxy, cookies, headers, etc.
    )  # send HTTP request and get HTTP response

    if response.status_code == requests.codes.OK:  # 200?
        data = response.json()  # convert JSON content to Python data structure
        for entry in data: # check for results
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = f'({entry.get("fl")})'
                    word_id = meta.get("id")
                    print(f"{word_id.upper()} {part_of_speech}")
                if "shortdef" in entry:
                    print('\n'.join(entry['shortdef']))
                print()
            else:
                print(entry)
        print('*' * 60)
        pprint(data)
        print('*' * 60)
    else:
        print("Sorry, HTTP response", response.status_code)

if __name__ == '__main__':
    main(sys.argv[1:])
