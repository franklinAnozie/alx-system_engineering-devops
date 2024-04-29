#!/usr/bin/python3
""" Show top ten reddit posts """

import requests


def top_ten(subreddit):
    """ gets the top ten reddits """
    URI = f"https://www.reddit.com/r/{subreddit}/top.json"
    header = {"User-Agent": "0x00"}
    req = requests.get(url=URI, headers=header, allow_redirects=False)
    if req.ok:
        try:
            retVal = req.json().get("data").get("children")
        except Exception:
            print(None)
            return
        else:
            if len(retVal) >= 10:
                for index in range(10):
                    print(retVal[index]["data"]["title"])
            else:
                for index in range(len(retVal)):
                    print(retVal[index]["data"]["title"])
    else:
        print(None)
        return
