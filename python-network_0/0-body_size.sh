#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
#Display size of body of response
#The size must be displayed in bytes
#You have to use curl
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
