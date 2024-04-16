#!/usr/bin/python3
""" Show top ten reddit posts """

import requests

def top_ten(subreddit="programming"):
    try:
        URI = f"https://www.reddit.com/r/{subreddit}/top.json"
        count = 10
        retVal = []
        req = requests.get(url=URI, allow_redirects=False)
        req = req.json()
    except Exception as e:
        retVal = 0
    else:
        for key in req:
            if key == "data":
                for mem in req[key]:
                    if mem == "children":
                        for nk in req[key][mem]:
                            while count > 0:
                                retVal.append(nk)
        print(len(retVal))


    finally:
        if retVal is None or retVal == 0:
            return 0
        else:
            return retVal

if __name__ == "__main__":
    top_ten()