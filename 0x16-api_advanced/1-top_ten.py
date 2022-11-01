#!/usr/bin/python3
""" this module get data from a reddit API """

import requests


def top_ten(subreddit):
    """ This function get data from API """
    headers = {'User-Agent': 'X-modhash'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
