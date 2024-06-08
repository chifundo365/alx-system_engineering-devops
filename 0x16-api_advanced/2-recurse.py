#!/usr/bin/python3
"""
Queries the Reddit API and processes its data
"""
import requests


def recurse(subreddit, hot_list=[], next=None):
    """Returns the title of subreddit in a listn"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 100}

    if next:
        params["after"] = next

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code >= 300:
        return None

    hot = response.json().get("data", {})
    next = hot.get("after")
    hot_items = hot.get("children", [])

    for item in hot_items:
        hot_list.append(item.get("data", {}).get("title", ""))

    if next:
        return recurse(subreddit, hot_list, next)
    else:
        return hot_list
