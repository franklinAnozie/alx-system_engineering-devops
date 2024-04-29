#!/usr/bin/python3
"""
    1-top_ten module
"""
import requests


def top_ten(subreddit):
    """
        take one arg the subreddit name
        sends a get req to an api
        to get the top 10
        returns value
    """
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {"User-Agent": "0x00"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.status_code != 200:
        print(None)
        return
    value = data.json().get("data")
    if value is None:
        print(None)
        return
    for post in value.get("children")[0:10]:
        print(post.get("data").get("title"))
