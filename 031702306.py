# encoding: utf-8
# -*- coding: utf-8 -*-
#!/usr/bin/python3
import unittest
import re
import fileinput
import cpca
import json
import numpy as np
# 自定义获取文本手机号函数
def get_findAll_mobiles(text):
    """
    :param text: 文本
    :return: 返回手机号列表
    """
    mobiles = re.findall(r"1\d{10}", text)
    return mobiles

#if __name__ == '__main__':

    
content = input()#content是一整行,moblies【0】是电话号码

for x in content:
    if x=='1':
        flag=1
        content=re.sub('1!','',content,1)
        break;
    elif x=='2':
        flag=2
        content=re.sub('2!','',content,1)
        break;
        
content = re.sub('\.','',content)#切除句号
moblies=get_findAll_mobiles(text=content)#把手机号分出来了
# 分出姓名
n=0
for x in content:
    if x!=',':
        n=n+1
    else:
        break;
name=content[:n]#把姓名分出来了，姓名是name
    
# 删除字符串中姓名、电话号码
content=re.sub(moblies[0],'',content,1)
content=re.sub(name,'',content,1)
content=re.sub(',','',content,1)
#content=re.sub('.','',content,1)
    
#用cpca库 分离地址
b=[]
b.append(content)
df = cpca.transform(b, cut=False)
df1=np.array(df)
df2=df.values.flatten()
df3=df2.tolist()
#把DataFrame转换成ndarray再转成list
 
#输出
    #print ('{"姓名":"',name,'","手机":"',moblies[0],r'","地址":',df3,'}') 
#    print (df3[3])
l=df3[3]
zhen = re.match('.+?(?:乡|镇|街道)',l)
if zhen != None :
    str = re.search('.+?(?:乡|镇|街道)',l).group()
    l = re.sub('.+?(?:乡|镇|街道)','',l)
else :
    str=''
road=l
df3[3] = str
df3.insert(4,road)

if flag == 2:
    zhen=re.match('.+?(?:街|巷|路)',l)
    if zhen != None:
        road = re.search('.+?(?:街|巷|路)',l).group()
        l=re.sub('.+?(?:街|巷|路)','',l)
    else:
        road=''
    df3[4]=road 
    zhen=re.match('.+?(?:号)',l)
    if zhen != None :
        num = re.search('.+?(?:号)',l).group()
        l = re.sub('.+?(?:号)','',l)
        rest = l
    else :
        num = ''

#print (rest)详细地址
    df3.insert(5,num)
    df3.insert(6,rest)
#print (df3)
d={}
d["姓名"]=name
d["手机"]=moblies[0]
d["地址"]=df3
json1=json.dumps(d,ensure_ascii = False)
print(json1)
