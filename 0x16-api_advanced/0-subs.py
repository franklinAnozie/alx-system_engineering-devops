#!/usr/bin/python3
""" Get the number of subcribers for a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ gets the number of subscribers """
    URI = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "ubuntu:Python (by/0x00)"}
    req = requests.get(url=URI, headers=header, allow_redirects=False)
    if req.ok:
        try:
            retVal = req.json().get("data").get("subscribers")
        except Exception:
            return 0
        else:
            return retVal
    else:
        return 0
