#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response decoded in utf8.

Requirements:
- You have to manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
