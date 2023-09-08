# -*- coding: utf-8 -*-
# @Author : pan
# @Description : 绘制轨迹
# @Date : 2023年7月27日10:46:25

from collections import deque

import cv2
import numpy as np

palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)
COLORS_10 =[(144,238,144),(178, 34, 34),(221,160,221),(  0,255,  0),(  0,128,  0),(210,105, 30),(220, 20, 60),
            (192,192,192),(255,228,196),( 50,205, 50),(139,  0,139),(100,149,237),(138, 43,226),(238,130,238),
            (255,  0,255),(  0,100,  0),(127,255,  0),(255,  0,255),(  0,  0,205),(255,140,  0),(255,239,213),
            (199, 21,133),(124,252,  0),(147,112,219),(106, 90,205),(176,196,222),( 65,105,225),(173,255, 47),
            (255, 20,147),(219,112,147),(186, 85,211),(199, 21,133),(148,  0,211),(255, 99, 71),(144,238,144),
            (255,255,  0),(230,230,250),(  0,  0,255),(128,128,  0),(189,183,107),(255,255,224),(128,128,128),
            (105,105,105),( 64,224,208),(205,133, 63),(  0,128,128),( 72,209,204),(139, 69, 19),(255,245,238),
            (250,240,230),(152,251,152),(  0,255,255),(135,206,235),(  0,191,255),(176,224,230),(  0,250,154),
            (245,255,250),(240,230,140),(245,222,179),(  0,139,139),(143,188,143),(255,  0,  0),(240,128,128),
            (102,205,170),( 60,179,113),( 46,139, 87),(165, 42, 42),(178, 34, 34),(175,238,238),(255,248,220),
            (218,165, 32),(255,250,240),(253,245,230),(244,164, 96),(210,105, 30)]
#颜色板
dic_for_drawing_trails = {}
def compute_color_for_labels(label):
    """
    设置不同类别的固定颜色
    """
    if label == 0: #person
        color = (85,45,255)
    elif label == 2: # Car
        color = (222,82,175)
    elif label == 3:  # Motobike
        color = (0, 204, 255)
    elif label == 5:  # Bus
        color = (0, 149, 255)
    else:
        color = [int((p * (label ** 2 - label + 1)) % 255) for p in palette]
    return tuple(color)

#绘制轨迹
def draw_trail(img, bbox, names,object_id, identities=None, offset=(0, 0)):
    try:
        for key in list(dic_for_drawing_trails):
            if key not in identities:
                dic_for_drawing_trails.pop(key)
    except:
        pass

    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]

        #获取锚框boundingbox中心点
        center = (int((x2+x1)/ 2), int((y2+y2)/2))

        #获取目标ID
        id = int(identities[i]) if identities is not None else 0
        #创建新的缓冲区
        if id not in dic_for_drawing_trails:
          dic_for_drawing_trails[id] = deque(maxlen= 64)
        try:
            color = compute_color_for_labels(object_id[i])
        except:
            continue

        dic_for_drawing_trails[id].appendleft(center)
        #绘制轨迹
        for i in range(1, len(dic_for_drawing_trails[id])):

            if dic_for_drawing_trails[id][i - 1] is None or dic_for_drawing_trails[id][i] is None:
                continue
            #轨迹动态粗细
            thickness = int(np.sqrt(64 / float(i + i)) * 1.5)
            img = cv2.line(img, dic_for_drawing_trails[id][i - 1], dic_for_drawing_trails[id][i], color, thickness)
    return img