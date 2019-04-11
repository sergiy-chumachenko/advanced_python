# -*- coding: utf-8 -*-
from functools import lru_cache
import urllib.error
import urllib.request


@lru_cache(maxsize=24)
def get_webpage(module):
    # Search module page
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


if __name__ == "__main__":
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)

        if page:
            print("{} page of the module has been found".format(module))
