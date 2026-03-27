#!/usr/bin/python3
"""Displays the value of X-Request-Id from the response header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
