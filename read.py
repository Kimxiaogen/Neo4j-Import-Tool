import string
import chardet

def readfile(path):
    l = []
    f = open(path,'r',encoding='UTF-8-sig')
    for t in f.readlines():
        t = t.strip('\n')
        arr = str.split(t,',')
        arr = list(filter(None,arr))
        l.append(arr)
    f.close()
    return l
