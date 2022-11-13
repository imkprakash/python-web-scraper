from bs4 import BeautifulSoup
import requests
count = 1   # Variable to store number of pages

# URL of the first page
url = "https://scrapingclub.com/exercise/list_basic/"

# Code to get data from the first page
print("Page No. {}".format(count))
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
for i in items:
    itemName = i.find("h4", class_="card-title").text.strip("\n")
    itemPrice = i.find("h5").text
    print("Price: {}, Item name = {}".format(itemPrice, itemName))

count += 1

# Getting all the pages that are present at the bottom of the webpage
pages = soup.find("ul", class_="pagination")
urls = []                               # Stores all the urls
links = pages.find_all("a", class_="page-link")
for link in links:
    # Checking if the page number is a digit, helps eliminating duplicate data
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        # Getting the hyperlink and storing it in the list urls
        x = link.get("href")
        urls.append(x)

# Iterating over every url stored in the list to get all the data
for i in urls:
    print("Page No. {}".format(count))
    newUrl = url + i            # Constructing the new url to get data
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    for i in items:
        itemName = i.find("h4", class_="card-title").text.strip("\n")
        itemPrice = i.find("h5").text
        print("Price: {}, Item name = {}".format(itemPrice, itemName))
    count += 1
