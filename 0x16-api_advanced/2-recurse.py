#!/usr/bin/python3
""" recursion """

import requests


def get_data(subreddit):
    """ gets the data to be used """
    retVal = None
    try:
        URI = f"https://www.reddit.com/r/{subreddit}/top.json"
        header = {"User-Agent": "0x00"}
        req = requests.get(url=URI, headers=header, allow_redirects=False)
    except Exception:
        retVal = None
    else:
        retVal = req.json().get("data").get("children")
    finally:
        if retVal is None:
            return retVal
        else:
            return retVal


def recursive_call(data, hot_list):
    """ recursively fills up the hot_list """
    if len(data) == 0:
        return hot_list
    hot_list.append(data[0]["data"]["title"])
    del (data[0])
    return recursive_call(data, hot_list)


def recurse(subreddit, hot_list=[]):
    """ gets the top reddits recursively """
    if not hot_list:
        hot_list = []
    data = get_data(subreddit)
    if data:
        return recursive_call(data, hot_list)
    else:
        return None
