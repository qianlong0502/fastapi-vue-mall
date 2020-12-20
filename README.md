## 说明
- 数据库采用MySQL
- 编程语言采用python， 后端框架采用最新的fastapi
- 前端采用html5、javascript、Ajax、vue.js
- [github地址](https://github.com/qianlong0502/fastapi-vue-mall)
## 环境要求
- python3.7+
- 所需第三方库均在requirements.txt中，运行前在项目路径下命令行中执行以下语句已安装所需第三方库
```commandline
pip install -r requirements.txt
```
## 数据库说明
- 使用数据库为MySQL
- 备份文件在项目目录下，文件名为 **backtry.sql** 
- 恢复数据库后，还需要更改文件`database.py`中的数据库URL代码方可正常运行，代码如下：
```python
SQLALCHEMY_DATABASE_URL: str = 'mysql+pymysql://root:root@localhost:3306/try?charset=utf8'
```
## 运行方法
- 确保Mysql数据库服务启动
- 在项目路径下执行如下代码以启动后端服务：
```commandline
python start.py
```
- 后端服务默认在8895端口运行，运行前可通过`netstat -ano`查看占用端口的进程从而解除占用
- 打开`static/index.html`文件进入登陆界面
- 初始账户为admin，密码为1234567