#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response, a header variable X-School-User-Id must be sent with the value of 98
curl -s -X GET -H "X-School-User-Id: 98" "$1"
