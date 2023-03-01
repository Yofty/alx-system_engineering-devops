#!/usr/bin/python3
"""
returns the number of subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    a  function that queries the Reddit API
    and returns the number of subscribers
    """

    if subreddit is None or not isinstance(dubreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
