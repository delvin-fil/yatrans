#!/usr/bin/env python3.8
import sys
import warnings
warnings.filterwarnings("ignore")
import requests

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                   'Firefox/14.0.1'),
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':
    'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':
    'gzip, deflate',
    'Connection':
    'keep-alive',
    'DNT':
    '1'
}

if len(sys.argv) < 2:
    print('Usage: tr.py -lf -t \n \
        -lf - language from-to \n \
        -t - text')
    sys.exit()

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate" 
KEY = "Это ваш API ключ" 
lf = sys.argv[1]
t = sys.argv[2]
def translate_me(mytext):
    params = {
    "key": KEY,
    "text": t,
    "lang": lf
    }
    response = requests.get(URL ,params=params, headers=headers)
    return response.json()

json = translate_me('test')
print(''.join(json['text']))
