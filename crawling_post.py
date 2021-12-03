import requests
from bs4 import BeautifulSoup
url = "https://ffoorreeuunn.tistory.com"

def parsing(url):
    
    string = requests.get(url)
    
    html = string.text
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

def extract(soup):
    pass

parsing(url)