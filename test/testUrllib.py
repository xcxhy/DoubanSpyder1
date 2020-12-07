import urllib.request

#获取一个get方式
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

#获取一个post请求
#
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url =url,data =data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
url = "http://www.douban.com"


req = urllib.request.Request(url =url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
