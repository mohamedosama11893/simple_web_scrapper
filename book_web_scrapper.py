"""
Book Web Scraper

A simple web scraping script that extracts book data from
https://books.toscrape.com/.

The script collects each book's title, rating, and price
using Requests and BeautifulSoup, then displays the results
in a clean, readable format.

This project demonstrates basic web scraping and HTML parsing
in Python.
"""
import requests
from bs4 import BeautifulSoup
#==== Adjust the request with the URL and BeautifulSoup Library=====#
# URL of the website to scrape
url = "https://books.toscrape.com/"

# Send a GET request to fetch the webpage
response = requests.get(url)

# Use .content (raw bytes) instead of .text to avoid encoding issues
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all book containers (each book is inside an <article> tag)
books = soup.find_all("article")

# Dictionary to map rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Loop through each book and extract details
for book in books:
    # Extract the book title from <h3> → <a> 'title' attribute
    title = book.h3.a['title']
    
    # Extract the book rating word and convert it to a number using rating_map
    rating_word = book.p['class'][1]
    rating = rating_map.get(rating_word, 0)  # default = 0 if not found
    
    # Extract the book price from <p class="price_color">
    price = book.find("p", class_="price_color").text

    # Handle singular/plural for stars
    star_text = "star" if rating == 1 else "stars"  
    
    # Print the result in a clean format
    print(f'Book title is: {title} | Rating: {rating} {star_text} | Price: {price}')
