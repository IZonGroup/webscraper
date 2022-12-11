# Import the BeautifulSoup library
from bs4 import BeautifulSoup

# Import the requests library
import requests

# Make a GET request to the website that you want to scrape
response = requests.get('https://www.example.com')

# Parse the HTML from the website using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the data that you want to scrape using BeautifulSoup's built-in methods
title = soup.find('h1').text
paragraph = soup.find('p').text

# Print the scraped data
print(title)
print(paragraph)
