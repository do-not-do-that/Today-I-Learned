import requests
from bs4 import BeautifulSoup


def deco_parsing(function):
    def parsing(urls):
        data = requests.get(urls[-1])

        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        return function(soup,urls)
    return parsing


@deco_parsing
def extract_post_title(soup,urls):
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
            urls.append(url)
            tags = extract_post_tag(urls)
            today_contents += f"<h2><a href={url}>{post_title}</a></h2>\n\n"
            for tag in tags:
                today_contents += f"#{tag}\n"
        break
            
    return today_contents

@deco_parsing
def extract_post_tag(soup,urls):
    tags = soup.select(".tag_content")[0].text.split(',\r\n')
    return tags


