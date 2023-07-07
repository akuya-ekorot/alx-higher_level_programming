#!/bin/bash
# Takes in a URL, sends a request to the URL and returns the size of the body response

curl -s ${1} | wc -c
