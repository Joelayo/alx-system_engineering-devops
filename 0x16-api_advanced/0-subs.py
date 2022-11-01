#!/usr/bin/python3
""" this module get data from a reddit API """

import requests


def number_of_subscribers(subreddit):
    """ This function get data from API """
    headers = {'User-Agent': 'X-modhash'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
