from uuid import uuid4
import hashlib


salt = uuid4().hex
cache = {}


# Механизм кэширования уже был показан на уроке :)
def get_cashed_url(url):
    if cache.get(url):
        print(f'Адрес {url} есть в кэшэ')
    else:
        hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = hashed_url
        print(f'Адреса {url} не было в кэше, однако уже занесён')


get_cashed_url('https://google.com')
get_cashed_url('https://google.com')
