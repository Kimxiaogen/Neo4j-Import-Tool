import os
import read
import solve

c = open('config.txt','r',encoding='UTF-8')
map={}
#读取配置信息#
for t in c.readlines():
    t = t.strip('\n')
    arr = str.split(t, '=')
    map[arr[0]] = arr[1]
url = map['url']
username = map['username']
password = map['password']
path = map['import_from']
#获取指定目录下可用csv文件#
list = []
r_list = []
dirs = os.listdir(path)
for d in dirs:
    if(os.path.splitext(d)[1] == '.csv'):
        list.append(path + '\\' + d)
#读取csv文件信息#
for l in list:
    r_list.append(read.readfile(l))
#插入关系#
for r in r_list:
    solve.insert(url,username,password,r)
c.close()