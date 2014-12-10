#!/usr/bin/python
# Simple CLI stock lookup using Google Finance and BeautifulSoup
# usage: ./ticker.py .dji .inx .ixic
import BeautifulSoup
import sys
import urllib2

symbols = sys.argv[1:]

url = 'http://finance.google.com/?q='

info = [
    'name',
    'tickerSymbol',
    'price',
    'priceChange',
    'priceChangePercent',
]

def colorize(val):
    red = '\033[0;31m{0}\033[00m'
    green = '\033[0;32m{0}\033[00m'
    white = '\033[0;37m{0}\033[00m'

    if val.startswith('-'):
        return red.format(val)
    elif val.startswith('+'):
        return green.format(val)

    if val.endswith('%'):
        if not val.startswith('-'):
            return green.format(val)
        else:
            return red.format(val)

    return white.format(val)


def parse_data(html):
    soup = BeautifulSoup.BeautifulSoup(html.read())
    for item in info:
        try:
            if item == 'priceChangePercent':
                results.append(
                    soup.find('meta', {'itemprop':item})['content']+'%'
                )
            else:
                results.append(
                    soup.find('meta', {'itemprop':item})['content']
                )
        except TypeError:
            print 'symbol not found.'
            break
   
 
if __name__ == '__main__':
    for symbol in symbols:
        results = []
        html = urllib2.urlopen(url + symbol)
        parse_data(html)
        for item in results:
            item = colorize(item)
            print item,
        print
