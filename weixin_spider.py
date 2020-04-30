from selenium import webdriver
import time
import urllib
from bs4 import BeautifulSoup

# import request
# from selenium.webdriver.common.keys import Keys


# options =webdriver.ChromeOptions
# # 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# # 更换头部
# options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# browser = webdriver.Chrome(chrome_options=options)

browser = webdriver.Chrome()
url = 'http://weixin.sogou.com/'
browser.get(url)
browser.maximize_window()

# 输入公众号名称
browser.find_element_by_xpath('//*[@id="query"]').send_keys("联华超市")
time.sleep(5)
# 点击搜索公众号按钮
browser.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]').click()
# 点击进入第一个公众号
browser.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/em').click()
# 点击进入公众号的第二篇文章
time.sleep(2)
# browser.find_element_by_xpath('//*[@id="history"]/div[1]/div[2]/div[2]').click()
handles = browser.window_handles
browser.switch_to_window(handles[1])
browser.find_element_by_xpath('//*[@id="WXAPPMSG1000000525"]/div/h4').click()
# 打印page_source
result = browser.page_source
# print(result)
# 定位图片的链接地址
data1  = browser.find_element_by_xpath('//*[@id="js_content"]/section/section[1]/section/section/img')
# print(data1)
# print(type(data1))

# 使用beautifulsoup 来寻找图片链接地址
soup = BeautifulSoup(result, 'html.parser')
# print(soup.prettify())
# 寻找所有带有<img>标签的链接 又或者是data_source
for link in soup.find_all('img'):
    img_url =link.get('data-src')
    print(img_url)
# img_url = r'https://mmbiz.qpic.cn/mmbiz_jpg/KPj0CktWHauwsK0aPYRc72pWbwG4Q5tHrM45Dr9QlOgc4JWtIuzrEeSspJJMfsQic3bJoWJNhiaAexUpiaXClQicwQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1'
# data2 = urllib.request.urlopen(img_url).read()
# f = open('stream.jpg', 'wb')
# f.write(data2)
# f.close()
# data2 = urllib.request.urlopen(dat)


time.sleep(10)
# browser.quit()
