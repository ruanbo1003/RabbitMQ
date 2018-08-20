
#一、连接 postgresql
psql -U postgres -h 127.0.0.1

#二、创建 DB 用户、设置密码
Create User 'robert' WITH PASSWORD 'robert'

#三、新建一个属于 robert 的数据库 company
Create Database company Owner robert;
