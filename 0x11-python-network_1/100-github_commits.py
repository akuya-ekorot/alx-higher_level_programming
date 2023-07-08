#!/usr/bin/env python3
"""Python script that takes 2 arguments that lists 10 commits (from the most
recent to oldest) of the repository and user passed in as argument using the
Github API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    req = requests.get(url)

    for i in range(10):
        print("{}: {}".format(req.json()[i].get('sha'),
                              req.json()[i].get('commit')
                              .get('author').get('name')))
