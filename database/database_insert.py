'''
from pymysql import *
con = connect(host="localhost",user="root",password="",db="college")
a = con.cursor()
roll = int(input("enter roll:"))
name=input("Enter name:")
course = input("Enter course:")
marks = int(input("Enter marks:"))
sql = "insert into student values(%d,'%s','%s',%d)"%(roll,name,course,marks)
a.execute(sql)
con.commit()
'''
