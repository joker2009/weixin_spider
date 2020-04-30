#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import time
from selenium import webdriver
from get_user_agent import UserAgent
import os
import datetime
import random
import logging
from logging.handlers import TimedRotatingFileHandler
import json
from PIL import Image


class WechatSpider(object):
    def __init__(self):
        # 添加日志# 设置日志的记录等级
        logging.basicConfig(level=logging.INFO)  # 调试debug级
        # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
        file_log_handler = TimedRotatingFileHandler("logs/log", backupCount=10, when='d')  # maxBytes=1024 * 1024 * 100,
        # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
        formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
        # 为刚创建的日志记录器设置日志记录格式
        file_log_handler.setFormatter(formatter)
        # 为全局的日志工具对象（flask app使用的）添加日志记录器
        logging.getLogger().addHandler(file_log_handler)

        self.cookie = 'ua_id=Trg5C4vqPB43Dmf5AAAAAPvSK79vbZmNx6GTeA_2C2w=; mm_lang=zh_CN; pgv_pv\
        i=6678697984; pgv_si=s1156800512; rewardsn=; wxtokenkey=777; sig=h014d5d93d56146b2f1bf7e5\
        e6e259f415f25796baefdecfc6fc831efe0e1ec41e9c61fe9aa46040e39'
        # self.driver = webdriver.Chrome(executable_path="/home/python/chromedriver")
        self.driver = webdriver.Chrome()
        self.current_time = datetime.datetime.now()  # '2018-07-07'
        self.user_agent = UserAgent()
        self.name = ['骆驼岭超市']
        with open('./time_record.config', 'r') as f:
            content = f.read()
        self.content = content

    def trans_fromat(self, path, old_img, new_imag):
        try:
            Image.open(path + old_img).save(path + new_imag)
        except Exception:
            logging.error('%s:图片格式转换失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        os.remove(path + old_img)

    def get_title_lable(self, public):
        headers = {
            'User-Agent': self.user_agent.get_user_agent(),  # .get_user_agent(),
            'Cookie': self.cookie
        }

        # 打开搜狗微信页面
        try:
            self.driver.get('http://weixin.sogou.com/')
            time.sleep(round(random.uniform(1, 3), 2))
        except Exception:
            logging.error('%s:打开http://weixin.sogou.com/页面失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        try:
            # 在输入框输入关键字
            self.driver.find_element_by_id('query').send_keys(public)
            time.sleep(round(random.uniform(1, 3), 2))
        except Exception:
            logging.error('%s:无法在输入框中输入搜索关键字' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        try:
            self.driver.find_element_by_class_name('swz2').click()
            time.sleep(round(random.uniform(1, 3), 2))
        except Exception:
            logging.error('%s:点击页面跳转失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        try:
            # 获取浏览器当前网页的标签
            handle = self.driver.current_window_handle
            # 点击搜索进入新的浏览器标签页
            self.driver.find_element_by_xpath("//a[@uigs='account_name_0']").click()
            time.sleep(round(random.uniform(1, 3), 2))

            # 获取所有的浏览器当前所有的标签页
            handles = self.driver.window_handles

            # 切换到新浏览器标签
            for new_handle in handles:
                if new_handle != handle:
                    self.driver.switch_to_window(new_handle)
        except Exception:
            logging.error('%s:浏览器内切换标签失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        time.sleep(round(random.uniform(5, 6), 2))

        # 获取十条信息的标签
        # a_tags = self.driver.find_elements_by_css_selector('.weui_media_bd')
        a_tags = self.driver.find_elements_by_class_name('weui_media_bd')
        print('当前公众号页面的文章数为：%s' % len(a_tags))

        # 获取当前的时间
        # current_time = str(datetime.datetime.now()).split(' ')[0]

        try:
            save_path = os.path.join(str(self.current_time).split(' ')[0], public)
            # 如果文件夹不存在
            if not os.path.exists(save_path):
                os.makedirs(save_path)
        except Exception:
            logging.error('%s:创建文件夹失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

        j = 0
        i = 1
        count = 0
        while j < len(a_tags):

            # 获取当前公众号页面的所有文章和文章日期
            a = self.driver.find_elements_by_css_selector('.weui_media_title')[j]
            art_time = self.driver.find_elements_by_css_selector('.weui_media_extra_info')[j]
            # print(a.get_attribute('textContent').strip())
            # print(art_time.get_attribute('textContent').strip())

            str_time = art_time.get_attribute('textContent').strip()
            pub_date = datetime.datetime.strptime(str_time, '%Y年%m月%d日').strftime('%Y-%m-%d')

            # 读取存储的数据，获取当前公众号最新文章的时间
            content = self.content

            if not content:
                content = '{}'
            json_data = json.loads(content)
            latest_time = json_data.get(public)

            if latest_time is None:
                latest_time = ''

            # 根据文章时间来判断有没有更新，有更新则爬取，没有则不在继续运行
            if pub_date > latest_time:
                count += 1
                try:
                    # 点击文章进入详情页
                    a.click()
                except Exception:
                    logging.error('%s:跳转到文章详情页失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

                # 获取该页所有图片的地址
                images_ele = self.driver.find_elements_by_tag_name('img')
                urls = [i.get_attribute('data-src') for i in images_ele if i.get_attribute('data-src') != None]
                for url in urls:
                    print(url)
                    time.sleep(round(random.uniform(1, 2), 2))

                    try:
                        response = requests.get(url, headers=headers)
                    except Exception:
                        logging.error('%s:请求图片失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)
                    file_type = response.headers['Content-Type']
                    file_type = file_type.split('/')[-1]

                    if file_type in ['webp', 'jpeg']:
                        try:
                            with open(save_path + '/' + str(i) + '.' + file_type, 'wb') as f:
                                f.write(response.content)
                        except Exception:
                            logging.error('%s:保存图片为本地文件失败' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), exc_info=True)

                        # 把格式为webp的图片转换成JPEG格式
                        if file_type == 'webp':
                            img_path = save_path + '/'
                            old_file = str(i) + '.' + file_type
                            new_file = str(i) + '.' + 'jpeg'
                            self.trans_fromat(img_path, old_file, new_file)

                    i += 1
            else:
                print('-----------------------')
                print('当前公众号今日没有新的文章')
                logging.error('当前公众号今日没有新的文章', exc_info=True)
                return
            j += 1
            # 回退到公众号文章列表页面
            self.driver.back()
        logging.error('当前公众号新增文章数为：%s' % count, exc_info=True)

        # 获取公众号最新文章时间，格式化保存
        date = self.driver.find_elements_by_css_selector('.weui_media_extra_info')[0].\
            get_attribute('textContent').strip()
        save_date = datetime.datetime.strptime(date, '%Y年%m月%d日').strftime('%Y-%m-%d')

        save_json = json.loads(content)
        save_json[public] = save_date
        with open('./time_record.config', 'w') as f:
            f.write('%s' % json.dumps(save_json))

        # 关闭浏览器
        self.driver.close()

    def start_working(self):
        print('++++++++++++++++++++++++++++++++++++++')
        print('0:自动抓取微信公众号  1：输入指定公众号抓取')
        button = input('请输入数字启动程序：')
        if str(button) == '0':
            action = input('确定执行此操作吗(y or n)?')
            if action == 'y':
                # for i in self.name:
                #     self.get_title_lable(i)
                self.get_title_lable(self.name[0])
            else:
                self.start_working()
        elif str(button) == '1':
            public = input('请输入公众号的名字或者ID：')
            action = input('确定执行此操作吗(y or n)?')
            if action == 'y':
                self.get_title_lable(public)
            else:
                self.start_working()
        else:
            print('\n')
            print('输入有误请从新输入!!!!!!!!')
            print('\n')
            self.start_working()


if __name__ == '__main__':
    spider = WechatSpider()
    spider.start_working()

