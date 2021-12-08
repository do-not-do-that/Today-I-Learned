import os
import datetime
from crawling_post import extract_post_title
from github import Github


access_token = os.environ['TIL_TOKEN']
repo_name = "Today-I-Learned"

urls = ["https://ffoorreeuunn.tistory.com"]

today = datetime.datetime.today().strftime("%Y.%m.%d")
issue_title = f"TIL(Today I Learned) : {today}"
issue_contents = extract_post_title(urls)
repository = Github(access_token).get_user().get_repo(repo_name)
repository.create_issue(title=issue_title, body=issue_contents)

