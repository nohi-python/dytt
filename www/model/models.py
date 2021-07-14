import sys
import time
import uuid

sys.path.append("..")
from common.db.orm import Model, StringField, BooleanField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


#     id varchar(30) primary key not null comment '主键',
#     name varchar(100) not null comment '名称',
#     uri varchar(200) comment '地址',
#     name_src varchar(100) comment '译名',
#     story_date varchar(100) comment '年代',
#     chandi varchar(100) comment '产地',
#     leibie varchar(100) comment '类别',
#     yuyan varchar(100) comment '语言',
#     zimu varchar(100) comment '字幕',
#     shangyinriqi varchar(100) comment '上映日期',
#     doubanpinfen varchar(100) comment '豆瓣评分',
#     imdbpinfen varchar(100) comment 'IMDb评分',
#     wenjiangeshi varchar(100) comment '文件格式',
#     shipinchicun varchar(100) comment '视频尺寸',
#     wenjiandaxiao varchar(100) comment '文件大小',
#     pianchang varchar(100) comment '片长',
#     daoyan varchar(200) comment '导演',
#     zhuyan varchar(1000) comment '主演',
#     jianjie varchar(1000) comment '简介',
#     huojian varchar(1000) comment '获奖情况'
class DyttMovie(Model):
    __table__ = 'DYTT_MOVIE'

    id = StringField(primary_key=True, ddl='varchar(30)')
    name = StringField(ddl='varchar(100)')
    name_src = StringField(ddl='varchar(100)')
    uri = StringField(ddl='varchar(200)')
    story_date = StringField(ddl='varchar(100)')
    chandi = StringField(ddl='varchar(100)')
    leibie = StringField(ddl='varchar(100)')
    yuyan = StringField(ddl='varchar(100)')
    zimu = StringField(ddl='varchar(100)')
    shangyinriqi = StringField(ddl='varchar(100)')
    doubanpinfen = StringField(ddl='varchar(100)')
    imdbpinfen = StringField(ddl='varchar(100)')
    wenjiangeshi = StringField(ddl='varchar(100)')
    shipinchicun = StringField(ddl='varchar(100)')
    wenjiandaxiao = StringField(ddl='varchar(100)')
    pianchang = StringField(ddl='varchar(100)')
    daoyan = StringField(ddl='varchar(100)')
    zhuyan = StringField(ddl='varchar(1000)')
    jianjie = StringField(ddl='varchar(1000)')
    huojian = StringField(ddl='varchar(1000)')
    created_at = FloatField(default=time.time)
    updated_at = FloatField(default=time.time)
