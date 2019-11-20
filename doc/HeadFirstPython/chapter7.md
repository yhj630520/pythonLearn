## python and mysql

1.mysql新建数据库和用户授权

```mysql
# 新建数据库
create database vsearchlogDB;
#新建用户
create user 'vsearch' identified by '***VSearch_123***';
#数据库授权
grant all privileges on vsearchlogDB.* to 'vsearch'@'%' with grant option;

flush privileges;

#使用新账户登录mysql创建表
CREATE TABLE log (
	id INT auto_increment PRIMARY KEY,
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	phrase VARCHAR(128) not NULL,
	letters VARCHAR(32) NOT NULL,
	ip VARCHAR(16) NOT NULL,
	browser_string VARCHAR(256) NOT NULL,
	results VARCHAR(64) NOT NULL
);
#查看表结构
describe log;

```

2. **import**语句不要在函数内部使用，这会导致每一次函数调用都会进行一次读入和执行