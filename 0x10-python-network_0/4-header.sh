#!/bin/bash
#takes in a URL as argument, sends a GET request to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
