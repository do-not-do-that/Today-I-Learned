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
    today_contents = '해당 날짜에 공부하여 올린 포스팅입니다.\n 더욱 자세한 내용은 <a href="https://ffoorreeuunn.tistory.com/">&#128279;여기</a>에서 확인하실 수 있습니다.\n\n'
    today_posts = soup.select(".item_category")
    url_prefix = "https://ffoorreeuunn.tistory.com"
    
    # 포스팅은 항상 최신순으로 정렬되어 있기때문에 조건문에 맞지 않는것이 생기면 바로 반복 탈출.
    for today_post in today_posts:
        post_date = today_post.select(".date")[0].text
        if ":" in post_date:
            post_title = today_post.select("strong")[0].text
            post_image = today_post.select(".item-thumbnail")[0]['style']
            post_image = post_image[22:-2]
            print(post_image)
            url_suffix = today_post.select("a")[0].attrs['href']
            url = url_prefix + url_suffix
            urls.append(url)
            tags = extract_post_tag(urls)
            today_contents += f"<br><br><br><br><br><a href={url}><h2>&#128079;{post_title}</h2></a><br><br>![image]({post_image})<br><br>"
            for tag in tags:
                today_contents += f"#{tag}　　　"
        else : break
            
    return today_contents

@deco_parsing
def extract_post_tag(soup,urls):
    tags = soup.select(".tag_content")[0].text.split(',\r\n')
    return tags

