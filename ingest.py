"""
Module to get tweets
"""
import json
import os
import requests

# A lot of this file is directly copied/refactored from the Recent-Search/recent_search.py file
# from the Twtiter API v2 repo

bearer_token = os.environ.get(
    "AAAAAAAAAAAAAAAAAAAAAM7nqgEAAAAApYh%2FsB5PyLGQyK6RyrN50RpeNJA%3Dn2vR5o\
        9gaLiPd4mOqQmeNe83vWMcnLggAQIhVRjaVGin9zPxJh")
SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

query_params = {
    'query': '#mauiwildfires',
    'tweet.fields': 'author_id'
}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    """
    Handles connection to url, specifically references SEARCH_URL above
    """
    response = requests.get(url, auth=bearer_oauth, params=params, timeout=10)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    """
    Makes connection to endpoint defined 
    """
    json_response = connect_to_endpoint(SEARCH_URL, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
