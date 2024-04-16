#!/usr/bin/python3
""" Get the number of subcribers for a subreddit """

import requests

def number_of_subscribers(subreddit):
    try:
        URI = f"https://www.reddit.com/r/{subreddit}/about.json"
        retVal = None
        req = requests.get(url=URI, allow_redirects=False)
        req = req.json()
    except Exception as e:
        retVal = 0
    else:
        for key in req:
            if key == "data":
                for mem in req[key]:
                    if mem == "subscribers":
                        retVal = req[key][mem]
    finally:
        if retVal is None or retVal == 0:
            return 0
        else:
            return retVal
