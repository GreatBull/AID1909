import pymysql

#  连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')

#  生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 打开文件
f = open('dict.txt')
args_list = []
for line in f:
    word = line.split(' ')[0]
    mean = line.split(' ', 1)[1]
    args_list.append((word, mean))
    
#  执行各种数据库sql操作
sql = "insert into words (word,mean) values(%s,%s)"
cur.executemany(sql, args_list)
db.commit()

#  关闭游标和数据库
cur.close()
db.close()
