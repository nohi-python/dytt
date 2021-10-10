#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import hashlib
import json
import logging
import time

__author__ = 'NOHI'

from common.config.config import configs
from common.exception.exception import ServiceException
from common.web.apis import Page
from common.web.coroweb import get, post
from model.models import DyttMovie
from dytt.Dytt import BeautifulPicture, Movie

' url handlers '

COOKIE_NAME = 'dytt'
_COOKIE_KEY = configs.session.secret


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


def user2cookie(user, max_age):
    '''
    Generate cookie str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


async def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


# 主页
@get('/')
async def index(request, *, page='1'):
    return {
        '__template__': 'index.html',
        'page_index': get_page_index(page),
    }


# API-电影列表
@get('/api/movies')
async def api_movies(*, page='1'):
    page_index = get_page_index(page)
    num = await DyttMovie.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    movies = await DyttMovie.findAll(orderBy='id desc', limit=(p.offset, p.limit))
    return dict(page=p, movies=movies)


# API 更新电影列表
@post('/api/movie/refresh')
async def api_refresh_movie(request, *, page='1'):
    logging.debug('api_refresh_movie')
    beauty = BeautifulPicture()  # 创建一个类的实例
    try:
        movies = await beauty.get_page()  #
    except ServiceException as r:
        print('  未知错误 %s' % (r))


    logging.debug("=====saveMovies:" + str(len(movies)))
    # 保存
    await saveMovies(movies)

    logging.debug("=====get_page_index:" + str(len(movies)))
    page_index = get_page_index(page)
    num = await DyttMovie.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    movies = await DyttMovie.findAll(orderBy='id desc', limit=(p.offset, p.limit))
    return dict(page=p, movies=movies)


# 保存电影列表
async def saveMovies(movies):
    for movie in movies:
        try:
            await saveMovie(movie)
        except Exception as e:
            logging.exception(e)
            continue


# 保存电影
async def saveMovie(movie):
    id = movie.id_str
    dytt_movie = await DyttMovie.find(id)
    if dytt_movie is not None:
        logging.debug('电影[%s][%s]已经存在' % (id, movie.pianmin))
        copyMovie(movie, dytt_movie)
        await dytt_movie.update()
    # 转换为
    dytt_movie = DyttMovie()
    copyMovie(movie, dytt_movie)
    logging.debug('========dytt_movie:' + json.dumps(dytt_movie, ensure_ascii=False))
    await dytt_movie.save()


def copyMovie(movie: Movie, dytt_movie: DyttMovie):
    # dytt_movie_dict = dytt_movie.__dict__
    # for key, value in movie.__dict__.items():
    #     if hasattr(dytt_movie, '_' + key):
    #         dytt_movie[key] = value
    dytt_movie.id = movie.getParameters('id_str')
    dytt_movie.name = movie.getParameters('title_str')
    dytt_movie.name_src = movie.getParameters('title_str')
    dytt_movie.zhuyan = movie.getParameters('zhuyan')
    dytt_movie.jianjie = movie.getParameters('jianjie')
    dytt_movie.yuyan = movie.getParameters('yuyan')
    dytt_movie.zimu = movie.getParameters('zimu')
    dytt_movie.chandi = movie.getParameters('chandi')
    dytt_movie.leibie = movie.getParameters('leibie')
    dytt_movie.doubanpinfen = movie.getParameters('doubanpinfen')
    dytt_movie.imdbpinfen = movie.getParameters('imdbpinfen')
    dytt_movie.wenjiangeshi = movie.getParameters('wenjiangeshi')
    dytt_movie.shangyinriqi = movie.getParameters('shangyinriqi')
    dytt_movie.wenjiandaxiao = movie.getParameters('wenjiandaxiao')
    dytt_movie.pianchang = movie.getParameters('pianchang')
    dytt_movie.daoyan = movie.getParameters('daoyan')
    dytt_movie.huojian = movie.getParameters('huojiang')
    dytt_movie.uri = movie.getParameters('uri_str')
    dytt_movie.story_date = movie.getParameters('niandai')
    dytt_movie.shipinchicun = movie.getParameters('_shipinchicun')
