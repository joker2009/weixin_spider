from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import os

# def getImgUrl(weixin_name):
#     """
#     :param spider_url: 需要爬取得公众号名称
#     :return: 返回图片链接数组
#     """
#     browser = webdriver.Chrome()
#     url = 'http://weixin.sogou.com/'
#     browser.get(url)
#     browser.maximize_window()
#
#     # 输入公众号的名称
#     browser.find_element_by_xpath('//*[@id="query"]').send_keys(weixin_name)
#     time.sleep(2)
#     # 点击搜索公众号按钮
#     browser.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]').click()
#     # 点击进入第一个公众号
#     browser.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/em').click()
#
#
#     time.sleep(2)
#     # 切换浏览器标签
#     handles = browser.window_handles
#     browser.switch_to_window(handles[1])
#     # 点击进入公众号的第二篇文章 后面要做成循环的，遍历
#     browser.find_element_by_xpath('//*[@id="WXAPPMSG1000000525"]/div/h4').click()
#     # 取当前网页源码
#     result = browser.page_source
#     # 使用soup来定位图片来链接地址
#     soup = BeautifulSoup(result, 'html.parser')
#
#     # 寻找所有带有<img>标签的链接
#     img_url_list = []
#     for link in soup.find_all('img'):
#         img_url = link.get('data-src')
#         img_url_list.append(img_url)
#         # print(img_url)
#     return img_url_list


# 根据图片地址来保存图片到本地
def savePic(img_url,save_path):
    """

    :param img_url: 网络图片地址
    :param save_path: 需要保存的本地地址
    :return: 空
    """
    os.chdir(save_path)
    for i in img_url:
        if i != None:
            data = requests.get(i).content
            f = open('random'+ str(time.time()) + '.jpg','wb')
            f.write(data)
            print("图片本地写入成功")
            f.close()
    return  None
# 创建以日期和公众号为分类的文件夹，同时返回当天文件夹路径
def createFloder(path,weixin_name):
    """
    :param path: 需要创建文件夹的路径
    :param weixin_name: 以微信公众号名称创建文件夹
    :return: 返回保存图片的文件夹路径
    """
    day_time = time.strftime("%Y%m%d")
    # print(time.strftime("%Y%m%d"))
    os.chdir(path)
    # print(os.getcwd())
    time_folder = os.getcwd() + '/'+ day_time
    name_folder = time_folder + '/'+ weixin_name
    if not os.path.exists(time_folder):
        os.makedirs(time_folder)
        print("---OK---done_time_folder")
        # img_path = os.getcwd()
        # print(img_path)
        os.makedirs(name_folder)
        print("--name_folder--done")
    else:
        if not os.path.exists(name_folder):
            os.makedirs(name_folder)
        else:
            print("name_folder ---exists")
        print("--day_folder--exists")
    return name_folder



# 取得全部文章的链接
def getArticleLink(weixin_name):
    """

    :param weixin_name: 需要爬取公众号的中文名
    :return: 返回该公众号每篇文章的完整地址链接
    """
    browser = webdriver.Chrome()
    url = 'http://weixin.sogou.com/'
    browser.get(url)
    browser.maximize_window()

    # 输入公众号的名称
    browser.find_element_by_xpath('//*[@id="query"]').send_keys(weixin_name)
    time.sleep(2)
    # 点击搜索公众号按钮
    browser.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]').click()
    # 点击进入第一个公众号
    browser.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/em').click()

    time.sleep(2)
    # 切换浏览器标签
    handles = browser.window_handles
    browser.switch_to_window(handles[1])
    article_page_source = browser.page_source
    # print(article_page_source)
    soup = BeautifulSoup(article_page_source, 'html.parser')

    # 寻找所有文章链接，并拼接成真实文章链接
    all_article_link = []
    for link in soup.find_all('h4'):
        article_link = link.get('hrefs')
        # print(article_link)
        all_article_link.append(article_link)
    # print(all_article_link)
    # all_article_link 是未拼接的文章地址链接
    # full_article_link 是完整文章地址链接
    full_article_link = []
    for apart_link in all_article_link:
        full_article_link.append(r'https://mp.weixin.qq.com' + apart_link)
    # print(full_article_link[0])
    print("------文章链接数组返回成功----")
    # 返回的是完整文章链接 数组
    return full_article_link

# 得到每篇文章的链接，通过一个个点开，获取内部图片链接
def getImgUrl(url_link):
    """

    :param url_link:给出文章链接
    :return: 返回图片链接，以供下载使用
    """
    browser = webdriver.Chrome()
    browser.get(url_link)
    browser.maximize_window()
    article_page = browser.page_source
    soup = BeautifulSoup(article_page,'html.parser')
    # 寻找所有带有<img>标签的链接
    img_url_list = []
    for link in soup.find_all('img'):
        img_url = link.get('data-src')
        img_url_list.append(img_url)
        # print(img_url)
    print("--图片链接获取成功--")
    return img_url_list


if __name__ == '__main__':
    weixin_name = '联华超市'
    # img_url = getImgUrl(weixin_name)
    # # print(img_url)
    #
    # file = r"D:\MyWorkSpace\weixin_spider\img"
    # path = createFloder(file,weixin_name)
    # print(path)
    # savePic(img_url,path)

    # 测试获取文章链接功能
    # link_data = getArticleLink(weixin_name)
    # print(link_data)
    # 测试通过

    # alpha
    path = 'D:\MyWorkSpace\weixin_spider\img'
    save_path = createFloder(path, weixin_name)
    article = getArticleLink(weixin_name) # 返回一个文章链接数组
    img_url_list = []
    for i in article:
        img = getImgUrl(i)
        img_url_list.append(img)
    print(img_url_list)
    print(img_url_list[0])
    for v in range(len(img_url_list)):
        savePic(img_url_list[v], save_path)
    # for link in img_url_list:
    #     print(link)
    #     save_path(link, save_path)








