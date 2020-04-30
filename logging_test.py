'''
取出对应的文本，然后用正则匹配出来img_url
'''
# for i in range(len):
# from bs4 import BeautifulSoup
#
# # 已经使用Beautifulsoup 实现了
# import time
# import os
# day_time = time.strftime("%Y%m%d")
# # print(time.strftime("%Y%m%d"))
# os.makedirs("d://" + day_time)

import logging  # 引入logging模块
import os.path
import time
# 第一步创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个handler 用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/logs/'
print(log_path)
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)
# 第三步 定义handle的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  # logging.basicConfig函数对日志的输出格式及方式做相关配置
fh.setFormatter(formatter)

# 将logger 添加到handler里面
logger.addHandler(fh)

# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')