#!/usr/bin/env python3

from urllib.parse import urlparse

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')

print(o)