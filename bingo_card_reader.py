from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import csv
import collections

def checkRows(array):
    counter = 0
    for x in range(5):
        if (array[x][1] == 'Loss'):
             break
        else
            counter += 1
        

with open("cards.csv", "r") as csvfile:
    
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        url = str(row[1])
        page = urlopen(url).read()

        soup = BeautifulSoup(page, features="lxml")
        table = soup.find("body")

        rows = table.find_all('tr')

        array = []
        cells = table.find_all("td", {"class": "cell"})
        for cell in cells:
            if (cell != None):
                a = cell.text.strip().encode()
                text = a.decode("utf-8")
                array.append([str(text), "Win"])

        # for item in array:
        #     # print(item)
        #     count = 0

        checkRows(array)


