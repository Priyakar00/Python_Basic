'''
from pymysql import *
con = connect("localhost","root","","college")
a = con.cursor()
roll = int(input("enter roll:"))
name=input("Enter name:")
course = input("Enter course:")
marks = int(input("Enter marks:"))
sql = "update student set roll=%d,name='%s',course='%s',marks=%d"%(roll,name,course,marks)
a.execute(sql)
con.commit()
'''
from pymysql import *
con = connect(host="localhost",user="root",password="",db="college")
a = con.cursor()
roll = int(input("enter roll:"))
name=input("Enter name:")
course = input("Enter course:")
marks = int(input("Enter marks:"))
sql = "update student set name='%s',course='%s',marks=%d where roll=6"%(name,course,marks)
#print(sql)
a.execute(sql)
con.commit()
print("data updated")
