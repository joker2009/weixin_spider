import  requests
import os
img_url = r'https://mmbiz.qpic.cn/mmbiz_jpg/KPj0CktWHauwsK0aPYRc72pWbwG4Q5tHrM45Dr9QlOgc4JWtIuzrEeSspJJMfsQic3bJoWJNhiaAexUpiaXClQicwQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1'
data2 = requests.get(img_url).content
f = open('data.webp', 'wb')
f.write(data2)
f.close()

#
# from urllib.request import urlopen,Request
#
# data3 = urlopen(img_url)
# f2= open('data2.webp', 'wb')
# f2.write(data3)
# f.close()
# os.mknod("data.webp")
# with open('data.webp’，‘wb') as f :
#     f.write(data2)
