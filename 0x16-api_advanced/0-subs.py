#!/usr/bin/python3
"""
    0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """
        take one arg the subreddit name
        sends a get req to an api
        to get the number of subscribers
        returns the number or zero if not exits
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:Python (by/AjwadG)"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.ok:
        value = data.json().get("data").get("subscribers")
        return value if value is not None else 0
    return 0
