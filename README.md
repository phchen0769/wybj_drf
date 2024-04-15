# remote_diagnosis_drf
# logs 目录为日志文件以及uwsgi和nginx运行时产生的临时文件。
# supervisor.conf 为supervisord工作时的配置文件
# uwsgi.ini 为uwsgi的配置文件 
# repositories 为alpine国内源文件
# requirements.txt为项目需要安装的依赖包


# 运行数据库
# docker run -d --name Mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /Volumes/myDriver/github/db:/var/lib/mysql mariadb:latest

# 运行项目
# python manage.py runserver 