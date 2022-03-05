## 持续集成


## 版本依赖

* Python 3.7.6
* django 3.2.9


## 项目目录

```bash
├── README.md         # 自述文件
├── manage.py         # 启动文件
├── requirements.txt  # 虚拟环境依赖包版本
├── db.sqlite3        # 配置文件
├── package.json      # package.json
├── devops            # 项目源文件
│   ├── asgi.py       # 
│   ├── settings.py   # 项目配置文件
│   ├── views.py      # 路由方法
│   └── urls.py       # 路由
│   └── wsgi.py       # 
├── front             # 前端项目
├── workflow          # 工作流文件
```

## 启动

* python3 manage.py runserver 

## 数据库操作

* python3 manage.py migrate

* python3 manage.py makemigrations


## 新建应用

* python3 manage.py startapp my_app

## 前端项目启动

* yarn dev

