#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration
"""

__author__ = 'NOHI'

import logging
import sys

sys.path.append("../..")
from config import config_default


class Dict(dict):
    """
    Simple dict but support access as x.y style.
    """

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D


configs = config_default.configs

try:
    from config import config_override

    configs = merge(configs, config_override.configs)
    logging.info(configs)
except ImportError:
    traceback.print_exc()
    pass

try:
    logging.info('参数个数为[%s]个参数。' % len(sys.argv))
    logging.info('参数列表:%s' % str(sys.argv))
    conf_file = ''
    if len(sys.argv) > 2:
        conf_file = sys.argv[1]
        logging.info('配置文件:%s' % conf_file)
        if conf_file == 'dev' :
            from config import config_dev
            configs = merge(configs, config_dev.configs)
        logging.info(configs)
    else:
        logging.info('没有指定配置文集的')
except ImportError:
    logging.error('加载配置文件[%s]异常' % conf_file)
    pass

configs = toDict(configs)
