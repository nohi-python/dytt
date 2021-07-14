# -*- coding : utf-8 -*-
# coding: utf-8
import json
import random

import requests


class IPProxyPool():
    def __init__(self):  # 类的初始化操作
        self.api = 'http://139.224.41.4:8000/'

    def get_ippool(self):
        rs = requests.get(self.api)
        return rs.json()

    def get_proxies(self):
        rs = self.get_ippool()
        proxies = {
            'http': '',
            'https': ''
        }
        index = random.randint(1, len(rs)/2 + 1)
        print(rs[index])
        proxies['http'] = 'http://' + rs[index][0] + ':' + str(rs[index][1])
        proxies['https'] = 'http://' + rs[index][0] + ':' + str(rs[index][1])
        return proxies


if __name__ == '__main__':
    ippool = IPProxyPool()
    rs = ippool.get_ippool()
    print(rs)
    print(type(rs))
    print(ippool.get_proxies())