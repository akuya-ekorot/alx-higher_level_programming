#!/bin/bash
# Takes in a URL, sends a request to the URL and displays the body of the response only if the status is 200
status=$(curl -sL -o /dev/null -w "%{http_code}" "$1"); if [ $status -eq 200 ]; then curl -sL "$1"; fi
