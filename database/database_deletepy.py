from pymysql import *
con = connect(host="localhost",user="root",password="",db="college")
a = con.cursor()
roll = int(input("enter roll:"))
sql="delete from student where roll=%d"%(roll)
a.execute(sql)
con.commit()
print("data deleted")

