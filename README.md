# 微信公众号爬取
目的： 爬取微信公众号中关于商品价格的图片

关键词：微信公众号 联华超市 价格图片

技术：
```Python selenium request Xpath Beautifulsoup```
正则就不要用了


要求：

* 爬取[联华超市公众号](zplhmarket)中商品价格图片

* 图片保存本地
  >暂时保存本地

* 本地建立层级目录，（爬取当天时间–公众号名称 –商品价格图片）

* 只有第一次爬取为_全部爬取_，后续只爬取最新图片

* 代码中设置 UserAgent 和 Sleep ,防止反爬机制

取得一个公众号内全部内链
目前只爬出来了单篇文章的全部图片链接

# 重写爬虫
* 将运行情况写入日志
* 使用cookie
* 配置一个config 用来记录爬过的文章
* 
* 图片转换方法
* 记得写异常报告 ，写入到log
* 




