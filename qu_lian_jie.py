'''
取出对应的文本，然后用正则匹配出来img_url
'''
# for i in range(len):
from bs4 import BeautifulSoup

# 已经使用Beautifulsoup 实现了
import time
import os
day_time = time.strftime("%Y%m%d")
# print(time.strftime("%Y%m%d"))
os.makedirs("d://" + day_time)