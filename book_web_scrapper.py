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
