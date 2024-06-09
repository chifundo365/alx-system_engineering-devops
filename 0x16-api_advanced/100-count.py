#!/usr/bin/python3
"""
Queries the Reddit APi and processes the returned data
"""
import requests


def sort_two_keywords(array, length):
    """sorts two keywords(two tuples) with the same value in a list"""
    for i in range(length):
        if i + 1 < length:
            if array[i][1] == array[i + 1][1]:
                if array[i][0][0] > array[i + 1][0][0]:
                    temp = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = temp


def count_words(subreddit, word_list):
    """
    prints times the supplied keywords are found in a subreddit title
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"Content-Type": "application/json",
               "User-Agent": "My-User-Agent"}
    params = {"limit": 100}
    count = {}

    def query_results(word_list, next=None):
        if next:
            params["after"] = next
        req = requests.get(url, headers=headers,
                           params=params, allow_redirects=False)

        if req.status_code < 300:
            hot = req.json().get("data")
            next = hot.get("after")
            titles = [
                child.get("data").get("title") for
                child in hot.get("children")
                ]
            word_list = set(word_list)

        for w in word_list:
            for title in titles:
                num = title.lower().count(w)
                if num > 0:
                    if count.get(w):
                        count[w] = count.get(w) + 1
                    else:
                        count[w] = 1
        if next is not None:
            query_results(word_list, next)

    query_results(word_list)
    results = list(sorted(count.items(),
                          key=lambda item: item[1], reverse=True))
    sort_two_keywords(results, len(results))
    [print(f"{k}: {v}") for k, v in results]
