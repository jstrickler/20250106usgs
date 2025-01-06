from multiprocessing.dummy import Pool
import requests

APOD_URL = "https://api.nasa.gov/planetary/apod"

API_KEY = "DEMO_KEY"
# Note: "DEMO_KEY" limits
#   30 requests per IP address per hour
#   50 requests per IP address per day
# Go to https://api.nasa.gov/index.html#signUp to get a personal API key

# API_KEY = "your-API-key-goes-here"
# Note: in real life, don't put API keys in code -- read from file or environment
API_KEY = "Pl7oquUEi7pS0mPyqOYWSA6wbOeDK11hmiK3Wais"

def fetch_apod(date):
    with requests.session() as session:
        session.params = {"api_key": API_KEY}   # set common params
        response = session.get(
            APOD_URL,
            params = {"date": date},
        )
        if response.status_code == requests.codes.OK:
            data = response.json()  # convert JSON to Python dictionary
            if data['media_type'] != 'image':  # onlyl d/l images
                return
            
            if "hdurl" in data:  # attempt to get HD version of image
                image_url = data["hdurl"]
            else:  # fall back to std definition
                image_url = data["url"]
            
            image_title = data['title']
            image_filename = f"{image_title.replace(' ', '_')}.jpg"
            response = session.get(image_url)
            if response.status_code == requests.codes.OK:
                with open(image_filename, 'wb') as image_out:
                    image_out.write(response.content)
            else:
                display_error(response, f"Bad image fetch for {image_url}")
        else:
            display_error(response, f"Bad date request for {date}")
        return response.status_code == requests.codes.OK

def display_error(response, message):
    print(f"Response error code: {response.status_code}")
    print(message)
    print(response.text)
    print("*" * 60)

