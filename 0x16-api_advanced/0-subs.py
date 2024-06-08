#!/usr/bin/python3
"""
Queries the RedditApi and processes its data
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers in a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    sub_r_subscribers = requests.get(url,
                                     headers=headers,
                                     allow_redirects=False
                                     )
    if sub_r_subscribers.status_code >= 300:
        return 0
    return sub_r_subscribers.json().get("data").get("subscribers")


print(number_of_subscribers("programming"))
