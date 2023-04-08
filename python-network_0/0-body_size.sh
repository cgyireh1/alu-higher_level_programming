#!/bin/bash
#script that takes in a URL, sends a request to that URL,and display size of body of response
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
