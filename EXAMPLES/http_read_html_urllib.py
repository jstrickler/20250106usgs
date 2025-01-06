from urllib.request import urlopen
import gzip

response = urlopen("https://www.python.org/")

print(response.info())  # .info() returns a dictionary of HTTP headers
print('-' * 60)

# read compressed raw content
zipped_raw_content = response.read()

# sometimes need to  uncompress content to get binary string (bytes object);
# sometimes it's not compressed
try:
    raw_content = gzip.decompress(zipped_raw_content)
except gzip.BadGzipFile as err:
    raw_content = zipped_raw_content

# decode bytes to get Python string
content = raw_content.decode('utf-8')

# show first 500 characters
print(content[:500])
