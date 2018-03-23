# !usr/bin/python
# -*- coding:UTF-8 -*-
# lichanglai

fo = open("source.txt","r+") # 打开文件
file = open("result.txt","w+")  # 打开文件
index = 0
for line in fo.readlines():  # 按行读取文件
    if (index%2 == 0):
         print "/// " + line.replace("\n","") 
         file.write("/// " + line.replace("\n","") + "\n")  # 写入文件
    else :
         print "@property (nonatomic, copy) NSString *" + line.replace("\n","") + ";" # 拼接字符串
         file.write("@property (nonatomic, copy) NSString *" + line.replace("\n","") + ";\n")  # 写入文件
    index += 1  # 下一行

# 关闭打开的文件
fo.close()