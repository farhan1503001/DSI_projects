#For connecting with database and creating table
#Creating database connection
import sqlite3
connection=sqlite3.connect('consumable.sqlite3')
curr=connection.cursor()
curr.execute('create table if not exists product(id integer primary key,name text not null,type text not null,start_date varchar(50),end_date varchar(50),total_consumption float,total_rating float,total_day_consumption integer default 0,status boolean default False )')
connection.close()
