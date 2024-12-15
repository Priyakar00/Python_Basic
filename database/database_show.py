from pymysql import *
con = connect(host="localhost",user="root",password="",db="college")
a = con.cursor()
sql = "select * from student"
'''
count = a.execute(sql)
for i in range(count):
    t = a.fetchone()
    #print(t)
    #print(t[0])
    for i in t:
        print(i,end="\t")
    print()
'''
a.execute(sql)
c=a.fetchall()
print(c)
for i in c:
    for j in i:
        print(j,end=' ')
    print()
con.commit()
