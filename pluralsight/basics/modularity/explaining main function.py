#!/usr/bin/env python3

"""
Retrieve and print words from a URL

usage:
    python3 test.py <url>

"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """ Fetch a list of words from url.
    Args:
        url: The url of a utf-8 text document.

    returns:
        A list of strings containing the words from document provided as url.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """
    print items one per line.

    Args: 
        An iterable series of printable items.
    """
    for word in items:
        print(word)

def main():
    """
    print each words from a text document from a URL.
    Args:
        url: The URL of UTF-* text document.
    """
    url = sys.argv[1] # Because sys.argv[0] consists of module filename itself.
    words = fetch_words(url)
    print_items(words)
    

if __name__ == "__main__":
    main()