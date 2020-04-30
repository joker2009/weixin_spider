# -*- coding:utf-8 -*-
import os
import time
import urllib
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.ivsky.com/tupian/')

os.mkdir('img')
os.chdir('img')
for x in range(1,3):
    print ('正在获取第{}页图片'.format(x))

    for i in range(1,5):
        i = float(i)/5
        print(i)
        js = "document.documentElement.scrollTop =document.documentElement.scrollHeight * %f"%i
        driver.execute_script(js)
        time.sleep(3)
    img_list = driver.find_elements_by_css_selector('.il_img a img')
    for img in img_list:
        img_scr = img.get('scr') # 这里报错，显示对象没有GET属性
        img_name = img.scr.split('/')[-1]
        urllib.urlretrieve(img_scr,img_name)
    driver.find_element_by_link_text('下一页').click()
os.chdir(os.path.pardir)
driver.quit()