import urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import csv

url = input('Enter - ')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen(url, context=ctx).read().decode('utf-8').splitlines() # read().decode('utf-8') is used to decode the bytes read from the URL into a string using UTF-8 encoding,  .splitlines() takes the '\n' charater as argument to split the string into a list of lines.


with open('stats.csv', 'w', newline="", encoding= 'utf-8') as file:
    writer = csv.writer(file, delimiter=",")
    for line in html:
        line = line.strip().replace("b'", "").replace("\\n'", "")
        reader = csv.reader([line])
        for row in reader:
            writer.writerow(row)

