import sys
import os
from urllib.request import urlopen
from urllib.error import HTTPError

# url to download a PDF file of a NASA ISS brochure

url = 'https://www.nasa.gov/wp-content/uploads/2021/12/sls_fact_sheet.pdf'  # target URL
saved_pdf_file = 'nasa.pdf'  # name of PDF file for saving
ile = 'nasa_iss.pdf'  # name of PDF file for saving

try:
    URL = urlopen(url)  # open the URL
except HTTPError as e:  # catch any HTTP errors
    print("Unable to open URL:", e)
    sys.exit(1)

pdf_contents = URL.read()  # read all data from URL in binary mode
URL.close()

with open(saved_pdf_file, 'wb') as pdf_in:
    pdf_in.write(pdf_contents)  # write data to a local file in binary mode

if sys.platform == 'win32':  # select platform and choose the app to open the PDF file
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    cmd = 'open ' + saved_pdf_file
else:
    cmd = 'acroread ' + saved_pdf_file

os.system(cmd)  # launch the app
