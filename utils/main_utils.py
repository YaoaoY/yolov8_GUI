import os
import re


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)

def check_url(img_url: str):
    """
    判断img_url路径是否含有中文字符
    :param img_url: 图片路径
    :return: True or False
    """
    result = re.search('[\u4e00-\u9fa5]', img_url)
    if result:
        return True
    else:
        return False

# 调用函数进行判断
url1 = 'example.jpg'
url2 = '示例路径/图片.jpg'
contains_chinese1 = check_url(url1)
contains_chinese2 = check_url(url2)
print(contains_chinese1)  # 输出 False
print(contains_chinese2)  # 输出 True

