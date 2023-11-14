import requests
import os
import json

# A lot of this file is directly copied/refactored from the Recent-Search/recent_search.py file
# from the Twtiter API v2 repo

bearer_token = os.environ.get(
    "AAAAAAAAAAAAAAAAAAAAAM7nqgEAAAAApYh%2FsB5PyLGQyK6RyrN50RpeNJA%3Dn2vR5o9gaLiPd4mOqQmeNe83vWMcnLggAQIhVRjaVGin9zPxJh")
SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

query_params = {
    'query': '#climatechange',
    'tweet.fields': 'author_id'
}
