#!/usr/bin/python3
"""script that takes in a URL and an email, 
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]

    requests = request.Request(url)
    with request.urlopen(requests) as response:
        header = "X-Request-Id"
        print(dict(response.headers).get(header))
