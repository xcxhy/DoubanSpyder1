#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

# pat = re.compile("AA") #此处的AA是正则表达式，用于去验证别的字符串
# m = pat.search("CAA")   #search字符串被校验的内容
#没有模式对象
#m = re.search("sad","Asad")#前面的字符串是规则，后面的字符串是被校验的对象


#print(re.findall("a","AFGSGaGSGaa"))#前面字符串是规则，后面字符串是被校验的

#print(re.findall("[A-Z]","AFGSGaGSGaa"))


#print(re.findall("[A-Z]+","AFGSGaGSGaa"))


#sub

#print(re.sub("a","A","abcdcasd"))  #找到小a用A替换，在第三个字符串查找

#建议在正则表达式中，被比较的字符串前面加r，不要担心字符转义的问题

a = r"\aabd-\'"
print(a)