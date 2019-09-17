# encoding: utf-8
# -*- coding: utf-8 -*-
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
def main():
    
    content = input()#content是一整行,moblies【0】是电话号码
    content = re.sub('\.','',content)#删除句号
    for x in content:
        if x=='1':
            test=1
            content=re.sub('1!','',content,1)
            break;
        elif x=='2':
            test=2
            content=re.sub('2!','',content,1)
            break;
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
    lgcon=df3[3]
    temp = re.match('.+?(?:镇|乡|街道)',lgcon)
    if temp != None :
        str4 = re.search('.+?(?:镇|乡|街道)',lgcon).group()
        lgcon = re.sub('.+?(?:镇|乡|街道)','',lgcon)
    else :
        str4=''
    str5=lgcon
    df3[3] = str4
    df3.insert(4,str5)
    #print (str4)
    #print(lgcon)
    if test == 2:
        temp=re.match('.+?(?:巷|路|街)',lgcon)
        if temp != None:
            str5 = re.search('.+?(?:巷|路|街)',lgcon).group()
            lgcon=re.sub('.+?(?:巷|路|街)','',lgcon)
        else:
            str5=''
        df3[4]=str5#路
        temp=re.match('.+?(?:号)',lgcon)
        if temp != None :
            str6 = re.search('.+?(?:号)',lgcon).group()
            lgcon = re.sub('.+?(?:号)','',lgcon)
            str7 = lgcon
        else :
            str6 = ''
    #print (str5)路
    #print (str6)号
    #print (str7)详细地址
        df3.insert(5,str6)
        df3.insert(6,str7)
    #print (df3)
    d={}
    d["姓名"]=name
    d["手机"]=moblies[0]
    d["地址"]=df3
    json1=json.dumps(d,ensure_ascii = False)
    print(json1)
main()