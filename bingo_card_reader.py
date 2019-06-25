from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

with open("cards.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))
