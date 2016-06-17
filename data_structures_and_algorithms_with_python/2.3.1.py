#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''List access timeing'''
import time
import random
import datetime

#----------------------------------------------------------------------
def main():
    """"""
    file=open("ListAccessTiming.xml","w")
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    file.write('<Plot title="Average List Element Access Time">\n')
    #这一部分处理时间
    #test list size 10-200
    xmin=10
    xmax=200
    #test list in xlist,time in ylist
    xlist=[]
    ylist=[]
    
    for x in range(xmin,xmax,10):
        xlist.append(x)
        prod=0
        
        #虚拟操作(创建X个0的列表)
        lst=[0]*x
        #停顿1秒为内存分配收回操作
        time.sleep(1)
        
        #开始时间
        starttime=datetime.datetime.now()
        #随机处理1000次
        for v in range(10):
            index = random.randint(0,x-1)
            var = lst[index]
            prod=prod*var
        #结束时间
        endtime=datetime.datetime.now()
        #处理时间
        deltaT=endtime-starttime
        #处理成秒
        accesstime=deltaT.total_seconds()*1000
        #添加到时间列表
        ylist.append(accesstime)
    file.write("    <Axes>\n")
    file.write('        <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">List Size</XAxis>\n')
    file.write('        <YAxis min="'+str(min(ylist))+'" max="'+str(60)+'">Microseconds</YAxis>\n')
    file.write("    </Axes>\n")
    file.write('    <Sequence title="Average Access Time vs List Size" color="red">\n')
    for i in range(len(xlist)):
        file.write('            <DataPoint x="'+str(xlist[i])+'" y="'+str(ylist[i])+'"/>\n')            
    file.write('    </Sequence>\n')
    #这一部分访问时间
    
    #收尾及关闭文件
    file.write('</Plot>\n')
    file.close()
if __name__ == "__main__":
    main()
    