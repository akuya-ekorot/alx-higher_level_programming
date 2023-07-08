#!/bin/bash
# Makes a request to the url passed as an argument, and responds with a message containing You got me!, in the body of the response
curl -sLX PUT --post{1..3} -d "user_id=98" -H "Origin: School" "$1"
