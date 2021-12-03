import os
import datetime
from crawling_post import extract_post_title
from github_utils import get_github_repo, upload_github_issue


access_token = os.environ['TIL_TOKEN']
repo_name = "Today-I-Learned"

urls = ["https://ffoorreeuunn.tistory.com"]

today = datetime.datetime.today().strftime("%Y.%m.%d")
issue_title = f"TIL(Today I Learned) : {today}"
issue_contents = extract_post_title(urls)
repository = get_github_repo(access_token, repo_name)
upload_github_issue(repository, issue_title, issue_contents)
