#!/usr/bin/python3
"""
Queries the reddit Api and processes the returned data
"""
import requests


def top_ten(subreddit):
    """Prints the titles of 10 hot subreddits"""
    headers = {"User-Agent": "My-User_Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    hot = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if hot.status_code >= 300:
        print(None)
    else:
        hot_list = hot.json().get("data").get("children")
        [print(item.get("data").get("title")) for item in hot_list]
