# 配置说明

我的项目在`/home/ubuntu/projects/Questionnaire`中,遇到配置时需要改成自己的路径

# nginx配置
在server中添加location
```
server{
    location /api {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:9000;
    }
    location /static {
        root /home/ubuntu/projects/Questionnaire/htmls;
    }
    location / {
        root  /home/ubuntu/projects/Questionnaire/htmls/front/;
        try_files $uri $uri/ /index.html;
        add_header Cache-Control no-store;
        index  index.html index.htm;
    }
}
```
> 注意: 上面的root后面的路径需要改成自己电脑中的路径

# uwsgi 配置
```
[uwsgi]
;项目目录
chdir=/home/ubuntu/projects/Questionnaire
module=Questionnaire.wsgi:application
master=true
pidfile=/tmp/project-master.pid
socket=127.0.0.1:8000
processes=5
harakiri=20
max-requests=5000
vacuum=true
;虚拟环境目录
home=/home/ubuntu/.djenv
```
> 注意: 上面的root后面的路径需要改成自己电脑中的路径

# 安装依赖包

## 构建虚拟环境

`virtualenv -p python3 /home/ubuntu/.djenv`

## 进入虚拟环境 

`source /home/ubuntu/.djenv/bin/activate`

## 安装依赖包

`pip install -r requirements.txt`

## 配置数据库

登录数据库: `mysql -uroot -p `

创建数据库: `create database questionnaire;`

创建数据库用户: `grant all on *.* to 'django'@'%' identified by 'djangopwd';`

构建迁移: `./manage.py makemigrations && ./manage.py migrate `

创建管理员: `./manage.py createsuperuser `

## 启动服务器

重启nginx: `sudo service nginx restart`

启动web服务器: `uwsgi --ini uwsgi.ini`

## 浏览器访问

`http://localhost`

