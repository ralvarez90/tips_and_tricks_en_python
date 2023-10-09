# -*- coding: utf-8 -*-
import pyshorteners

"""ACORTADORES DE URLS

Existe una librería llamada pyshorteners para acortar urls. La
dependencia es:
pip install pyshorteners
"""


def shorter_url(url: str):
    pys = pyshorteners.Shortener()
    short_url = pys.tinyurl.short(url)
    return short_url


# run program
if __name__ == '__main__':

    # url a acortar
    url = 'https://www.npmjs.com/package/@types/node'
    new_url = shorter_url(url=url)
    print(new_url)
