"""Fetch three pages at the same time.

Run this file from the terminal:

    python 28_learn_fetching_pages.py

map gives fetch_page one URL string per call. That is the same rule as
a thread argument: args=(url,) is a tuple of one URL. args=(url) is
only the string, so Python would pass every character as its own
argument.

These calls spend their time waiting for a website, so threads are a
good fit. The with block shuts the pool down after the pages return.

    url 1 --+
    url 2 --+-- map --> fetch_page(one full url) --> print the length
    url 3 --+
"""

from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


urls = [
    "https://docs.langchain.com/langsmith/agent-registry",
    "https://docs.langchain.com/langsmith/create-an-agent",
    "https://docs.langchain.com/langsmith/evaluation",
]


def fetch_page(url):
    # one full URL arrives here, not one character at a time
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, "html.parser")
    return f"{len(soup.text)} characters from {url}"


with ThreadPoolExecutor(max_workers=3) as executor:
    # map passes urls[0], then urls[1], then urls[2]
    for line in executor.map(fetch_page, urls):
        print(line)

print("All are fetched")
