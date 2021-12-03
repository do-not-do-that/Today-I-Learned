import requests
from bs4 import BeautifulSoup
url = "https://ffoorreeuunn.tistory.com"

def parsing(url):
    
    string = requests.get(url)
    
    html = string.text
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

def extract_post_title(soup):
    today_contents = ''
    today_posts = soup.select(".item_category")
    url_prefix = "https://ffoorreeuunn.tistory.com"
    
    # 포스팅은 항상 최신순으로 정렬되어 있기때문에 조건문에 맞지 않는것이 생기면 바로 반복 탈출.
    for today_post in today_posts:
        post_date = today_post.select(".date")[0].text
        if ":" in post_date:
            post_title = today_post.select("strong")[0].text
            url_suffix = today_post.select("a")[0].attrs['href']
            url = url_prefix + url_suffix
            today_contents += f"<h2><a href={url}>{post_title}</a></h2>\n\n"
        break
            
    return today_contents


print(extract(parsing(url)))