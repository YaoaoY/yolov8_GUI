# -*- coding: utf-8 -*-
# @Author : pan
# @Description : Flask工具包
# @Date : 2023年7月30日08:25:39
import hashlib
import json
import os
import string
import random
import cv2

from datetime import datetime
from typing import Any
from PIL import Image

from classes.sql_connect import SQLManager


def check_stream_availability(url):
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        cap.release()
        return True
    return False

def save_img_base64(image_data, path):
    # 格式化日期为指定样式（"YYYY-MM-DD"） 【获取当前日期】
    formatted_date = datetime.now().date().strftime("%Y-%m-%d")

    # 保存路径创建
    save_dir = f"{path}/{formatted_date}/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 生成新的文件名
    new_file_name = f"{(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))}_" \
                    f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}"

    # 完整路径
    output_path = save_dir + new_file_name + '.png'

    # 保存图片
    with open(output_path, 'wb') as file:
        file.write(image_data)

    return output_path

def save_img(name, img, path):
    # 格式化日期为指定样式（"YYYY-MM-DD"） 【获取当前日期】
    formatted_date = datetime.now().date().strftime("%Y-%m-%d")

    #保存路径创建
    save_dir = f"{path}/{formatted_date}/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 生成新的文件名
    new_file_name = f"{(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))}_" \
                    f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}_{name}"

    # 完整路径
    output_path = save_dir + new_file_name
    # 保存图片
    Image.fromarray(img).save(output_path)

    return output_path

# 200
def wrap_ok_return_value(data: Any) -> str:
    return json.dumps({
        'code': 200,
        'msg': '执行成功！',
        'data': data
    })

# 500
def wrap_error_return_value(message: str) -> str:
    return json.dumps({
        'code': 500,
        'msg': message,
        'data': None
    })

# 未授权状态码 401
def wrap_unauthorized_return_value(message: str) -> str:
    return json.dumps({
        'code': 401,
        'msg': message,
        'data': None
    })