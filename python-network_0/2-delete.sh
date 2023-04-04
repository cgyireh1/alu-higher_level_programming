#!/bin/bash
#Write a Bash script that sends a DELETE request to the URL passed as the first argument 
#Displays the body of the response
#ou have to use curl
curl -sX DELETE "$1"
