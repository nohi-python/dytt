# -*- coding : utf-8 -*-
# coding: utf-8
import json
import logging;
import random
import re
import traceback

from common.ippool.proxypool import IPProxyPool
from common.config.config import configs
import os
import time

import requests
from bs4 import BeautifulSoup

TITLE = {'◎译名': 'yimin', '◎片名': 'pianmin',
         '◎年代': 'niandai', '◎产地': 'chandi',
         '◎类别': 'leibie', '◎语言': 'yuyan',
         '◎字幕': 'zimu', '◎上映日期': 'shangyinriqi',
         '◎豆瓣评分': 'doubanpinfen', '◎IMDb评分': 'imdbpinfen',
         '◎文件格式': 'wenjiangeshi', '◎视频尺寸': 'shipinchicun',
         '◎文件大小': 'wenjiandaxiao', '◎片长': 'pianchang',
         '◎导演': 'daoyan', '◎主演': 'zhuyan',
         '◎简介': 'jianjie', '◎获奖情况': 'huojiang'}


class Movie(object):

    def __init__(self) -> None:
        super().__init__()

    def setParameters(self, key, value):
        self.__setattr__(key, value)

    def getParameters(self, key):
        return getattr(self, key, None)

    @property
    def id_str(self):
        return self._id_str

    @property
    def uri_str(self):
        return self._uri_str

    @property
    def title_str(self):
        return self._title_str

    @property
    def downloadUrl(self):
        return self._downloadUrl

    # 译名
    @property
    def yimin(self):
        return self._yimin

    # 片名
    @property
    def pianmin(self):
        return self._pianmin

    # 年代
    @property
    def niandai(self):
        return self._niandai

    # 产地
    @property
    def chandi(self):
        return self._chandi

    # 类别
    @property
    def leibie(self):
        return self._leibie

    # 语言
    @property
    def yuyan(self):
        return self._yuyan

    # 字幕
    @property
    def zimu(self):
        return self._zimu

    # 上映日期
    @property
    def shangyinriqi(self):
        return self._shangyinriqi

    # 豆瓣评分
    @property
    def doubanpinfen(self):
        return self._doubanpinfen

    # IMDb评分
    @property
    def imdbpinfen(self):
        return self._imdbpinfen

    # 文件格式
    @property
    def wenjiangeshi(self):
        return self._wenjiangeshi

    # 视频尺寸
    @property
    def shipinchichun(self):
        return self._shipinchichun

    # 文件大小
    @property
    def wenjiandaxiao(self):
        return self._wenjiandaxiao

    # 片长
    @property
    def pianchang(self):
        return self._pianchang

    # 导演
    @property
    def daoyan(self):
        return self._daoyan

    # 主演
    @property
    def zhuyan(self):
        return self._zhuyan

    # 简介
    @property
    def jianjie(self):
        return self._jianjie

    # 获奖情况
    @property
    def huojiang(self):
        return self._huojiang

    @id_str.setter
    def id_str(self, id_str):
        self._id_str = id_str

    @uri_str.setter
    def uri_str(self, uri_str):
        self._uri_str = uri_str

    @title_str.setter
    def title_str(self, title_str):
        self._title_str = title_str

    @downloadUrl.setter
    def downloadUrl(self, downloadUrl):
        self._downloadUrl = downloadUrl

    # 译名
    @yimin.setter
    def yimin(self, yimin):
        self._yimin = yimin

    # 片名
    @pianmin.setter
    def pianmin(self, pianmin):
        self._pianmin = pianmin

    # 年代
    @niandai.setter
    def niandai(self, niandai):
        self._niandai = niandai

    # 产地
    @chandi.setter
    def chandi(self, chandi):
        self._chandi = chandi

    # 类别
    @leibie.setter
    def leibie(self, leibie):
        self._leibie = leibie

    # 语言
    @yuyan.setter
    def yuyan(self, yuyan):
        self._yuyan = yuyan

    # 字幕
    @zimu.setter
    def zimu(self, zimu):
        self._zimu = zimu

    # 上映日期
    @shangyinriqi.setter
    def shangyinriqi(self, shangyinriqi):
        self._shangyinriqi = shangyinriqi

    # 豆瓣评分
    @doubanpinfen.setter
    def niandai(self, doubanpinfen):
        self._doubanpinfen = doubanpinfen

    # IMDb评分
    @imdbpinfen.setter
    def imdbpinfen(self, imdbpinfen):
        self._imdbpinfen = imdbpinfen

    # 文件格式
    @wenjiangeshi.setter
    def wenjiangeshi(self, wenjiangeshi):
        self._wenjiangeshi = wenjiangeshi

    # 视频尺寸
    @shipinchichun.setter
    def shipinchichun(self, shipinchichun):
        self._shipinchichun = shipinchichun

    # 文件大小
    @wenjiandaxiao.setter
    def wenjiandaxiao(self, wenjiandaxiao):
        self._wenjiandaxiao = wenjiandaxiao

    # 片长
    @pianchang.setter
    def niandai(self, pianchang):
        self._pianchang = pianchang

    # 导演
    @daoyan.setter
    def daoyan(self, daoyan):
        self._daoyan = daoyan

    # 主演
    @zhuyan.setter
    def zhuyan(self, zhuyan):
        self._zhuyan = zhuyan

    # 简介
    @jianjie.setter
    def jianjie(self, jianjie):
        self._jianjie = jianjie

    # 获奖情况
    @huojiang.setter
    def huojiang(self, huojiang):
        self._huojiang = huojiang


def _print(msg, *args):
    if args is None or len(args) == 0:
        logging.debug(msg)
    else:
        logging.debug('%s %s' % (msg, args))


class BeautifulPicture():
    def __init__(self):  # 类的初始化操作
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
        self.web_url = 'https://www.dy2018.com'  # 地址网站
        self.web_url_first = 'https://www.dy2018.com/html/gndy/dyzz/index.html'  # 要访问的网页地址
        self.web_url_page = 'https://www.dy2018.com/html/gndy/dyzz/index_%s.html'  # 要访问的网页地址
        self.folder_path =  configs.folder_path  # 设置图片要存放的文件目录
        self.ippool = IPProxyPool()
        # self.ippool = IPProxyPool_XXY()

    def request(self, url):  # 返回网页的response
        headers = {
            'User-Agent': random.choice(self.USER_AGENTS),
            # ':authority': 'www.dy2018.com',
            # ':method': 'GET',
            # ':path': '/html/gndy/dyzz/index.html',
            # ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.dy2018.com/html/gndy/dyzz/index.html',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        print(headers)
        # proxies = self.ippool.get_proxies()
        # r = requests.get(url, proxies=proxies, headers=headers, verify=False)  # 像目标url地址发送get请求，返回一个response对象
        r = requests.get(url, headers=headers, verify=False)  # 像目标url地址发送get请求，返回一个response对象
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            _print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            _print('创建成功！')
        else:
            _print(path, '文件夹已经存在了，不再创建')

    def save_img(self, url, name):  # 保存图片
        _print('开始保存图片...')
        img = self.request(url)
        time.sleep(5)
        file_name = name + '.jpg'
        _print('开始保存文件')
        f = open(file_name, 'ab')
        f.write(img.content)
        _print(file_name, '文件保存成功！')
        f.close()

    def get_page(self, pageIndex=1):
        logging.debug('开始请求第%s页', pageIndex)
        url = self.web_url_first
        if pageIndex > 1:
            url = self.web_url_page % pageIndex
        logging.debug('第%s页url[%s]', pageIndex, url)

        r = self.request(url)
        content = r.content.decode('gbk')
        # 模拟
        # file_name = '/Users/nohi/Downloads/first.html'
        # content = ''
        # try:
        #     with open(file_name, 'r', encoding='gbk') as f:
        #         content = content + f.read()
        # finally:
        #     if f:
        #         f.close()
        logging.debug(content)
        logging.debug("解析文件内容 start")
        all_a = BeautifulSoup(content, 'lxml').find_all('a', class_='ulink')  # 获取网页中的class为cV68d的所有a标签
        if not all_a or len(all_a) == 0:
            _print('结果为空')
            return
        else:
            _print('all_a', len(all_a))
        _print('开始创建文件夹')

        self.mkdir(self.folder_path)  # 创建文件夹
        _print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹
        i = 1  # 后面用来给图片命名
        p1 = re.compile(r'[《](.*?)[》]', re.S)  # 最小匹配
        movies = []
        for a in all_a:
            uri_str = a['href']  # a标签中完整的style字符串
            id_str = re.findall('\d+', uri_str)[0]
            title_str = a['title']  # a标签中完整的style字符串
            title_str = re.findall(p1, title_str)[0]
            uri_str = self.web_url + uri_str
            i += 1
            _print('id[%s],url[%s],name[%s]' % (id_str, uri_str, title_str))
            movie = Movie()
            movie.id_str = id_str
            movie.uri_str = uri_str
            movie.title_str = title_str
            ts = random.randint(5, 10)
            _print('sleep %ss' % ts)
            time.sleep(ts)
            movie = self.get_movie(movie)
            movies.append(movie)

        logging.debug('返回电影记录数:%s' % len(movies))
        return movies

    def get_movie(self, movie):
        _print('获取电影[%s][%s]' % (movie.title_str, movie.uri_str))
        url = movie.uri_str

        # 发送http请求
        r = self.request(url)
        content = r.content.decode('gbk')
        # 模拟
        # file_name = '/Users/nohi/Downloads/movie.html'
        # content = ''
        # try:
        #     with open(file_name, 'r', encoding='gbk') as f:
        #         content = content + f.read()
        # finally:
        #     if f:
        #         f.close()
        logging.debug(content)
        _print("解析文件内容 start")
        soap = BeautifulSoup(content, 'lxml')
        # 获取下载地址
        downloadList = soap.select('#downlist a')  # 获取网页中的class为cV68d的所有a标签
        for url in downloadList:
            # soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
            # logging.debug(url)
            _print('==============' + url.string)
        # 图片
        imgs = soap.select('#Zoom>img')
        for img in imgs:
            _print('==============' + img['src'])
        #
        _print('===> 电影信息')
        strings = soap.select('#Zoom')[0].stripped_strings

        # for key, value in TITLE.items():
        #     _print('[%s][%s]' % (key, value))

        zhuyan = False
        jianjie = False
        huojiang = False

        for line in strings:
            try:
                line = line.replace('　', '')
                print(line + ' ===> ', end='')

                pre_str = line[0:3]
                print(pre_str, end='')
                if pre_str == '◎文件':
                    pre_str = line[0:4]

                key = self.getKey(pre_str)
                if key is None:
                    if zhuyan:
                        movie.zhuyan = movie.zhuyan + ' ' + line
                    if jianjie:
                        movie.jianjie = movie.jianjie + '' + line
                    if huojiang:
                        movie.huojiang = movie.huojiang + '' + line
                    continue
                else:
                    zhuyan = False
                    jianjie = False
                    huojiang = False

                value = TITLE.get(key)
                key_len = len(key)
                print('->' + key + ':' + value + ', key_len:' + str(key_len), end='')
                movie.setParameters('_' + value, line[key_len:])

                print(' ----->>>>>> ' + movie.getParameters('_' + value))
                if key == '◎主演':
                    zhuyan = True
                    continue
                if key == '◎简介':
                    jianjie = True
                    continue
                if key == '◎获奖情况':
                    huojiang = True
                    continue
            except Exception as r:
                traceback.print_exc()
                print('  未知错误 %s' % (r))
        print('=========================')
        print(json.dumps(movie, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False))
        return movie

    def getKey(self, pre):
        for key, value in TITLE.items():
            if key.find(pre) == 0:
                return key


if __name__ == '__main__':
    beauty = BeautifulPicture()  # 创建一个类的实例
    beauty.get_page()  #
    # movie = Movie()
    # movie.id_str = '103711'
    # movie.uri_str = 'https://www.dy2018.com/i/103711.html'
    # movie.title_str = '阳光劫匪'

    # beauty.get_movie(movie)  # 执行类中的方法
