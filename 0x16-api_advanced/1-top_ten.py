#!/usr/bin/python3
""" Show top ten reddit posts """

import requests


def top_ten(subreddit):
    """ gets the top ten reddits """
    try:
        URI = f"https://www.reddit.com/r/{subreddit}/top.json"
        header = {"User-Agent": "0x00"}
        count = 10
        retVal = []
        req = requests.get(url=URI, headers=header, allow_redirects=False)
        req = req.json()
    except Exception as e:
        retVal = 0
    else:
        for key in req:
            if key == "data":
                for mem in req[key]:
                    if mem == "children":
                        for nk in req[key][mem]:
                            if count <= 0:
                                break
                            retVal.append(nk["data"]["title"])
                            count -= 1
    finally:
        if retVal == 0 or len(retVal) == 0:
            print(None)
        else:
            for x in retVal:
                print(x)
