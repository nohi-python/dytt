# dytt
> create by nohi 20210713

## 模块
```
├── config
│   ├──config_default.py                    # 默认配置文件
│   └── config_override.py                  # 配置文件，优先级高于default
├── dist                                    # 打包后目录
├── script                                  # 数据库初始化脚本
├── test                                    # 测试目录
├── www                                     # 应用主目录
│   ├── static                              # 静态文件
│   ├── common                              # 公用模块
│   │   ├── config                          # 配置文件解析代码
│   │   ├── db                              # 数据库解析
│   │   └── web                             # http解析
│   ├── model                               # 模型层
│   ├── templates                           # 视图模板
│   ├── app.py                              # 程序入口函数
│   └── handlers.py                         # api注册
├── .gitignore                              # Git忽略文件
└──  README.md                              # 说明文档
```

## 功能点
* 主页：http://127.0.0.1:9010/?t=1626268424653&page=1
* 更新：获取电影天堂电影页列表

## 进程监控
* Supervisor
## 自动发布
* fab build
* fab deploy
