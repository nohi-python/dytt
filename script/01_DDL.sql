create table DYTT_MOVIE
(
    id            varchar(30) primary key not null comment '主键',
    name          varchar(100)            not null comment '名称',
    uri           varchar(200) comment '地址',
    name_src      varchar(100) comment '译名',
    story_date    varchar(100) comment '年代',
    chandi        varchar(100) comment '产地',
    leibie        varchar(100) comment '类别',
    yuyan         varchar(100) comment '语言',
    zimu          varchar(100) comment '字幕',
    shangyinriqi  varchar(100) comment '上映日期',
    doubanpinfen  varchar(100) comment '豆瓣评分',
    imdbpinfen    varchar(100) comment 'IMDb评分',
    wenjiangeshi  varchar(100) comment '文件格式',
    shipinchicun  varchar(100) comment '视频尺寸',
    wenjiandaxiao varchar(100) comment '文件大小',
    pianchang     varchar(100) comment '片长',
    daoyan        varchar(200) comment '导演',
    zhuyan        varchar(1000) comment '主演',
    jianjie       varchar(1000) comment '简介',
    huojian       varchar(1000) comment '获奖情况',
    created_at    real not null comment '创建时间',
    updated_at    real not null comment '更新时间'
)