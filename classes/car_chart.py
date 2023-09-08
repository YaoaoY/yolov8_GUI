# -*- coding: utf-8 -*-
# @Author : pan
# @Description : 动态图（还有bug）
# @Date : 2023年7月27日10:28:50

import time

from PySide6.QtCore import QThread, Signal

import matplotlib.pyplot as plt
# mplcyberpunk不可去掉！
import mplcyberpunk
import matplotlib
matplotlib.use('TkAgg')


class WorkerThread(QThread):
    # finished = Signal()
    # count_signal = Signal()  # 数据信号

    def __init__(self):
        super().__init__()
        self.is_stopped = True
        self.is_continue = True
        self.is_close = True
        self.is_exec = True

    # 线程执行
    def run(self):
        self.is_stopped = False
        self.is_continue = False
        self.is_close = False
        self.is_exec = False

        # 添加样式 赛博朋克
        plt.style.use("cyberpunk")
        # plt显示中文
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 隐藏默认的工具栏
        plt.rcParams['toolbar'] = 'None'
        plt.figure("MTSP系统动态图表")

        fig = plt.gcf()
        # 注册窗口关闭事件的回调函数
        fig.canvas.mpl_connect("close_event", self.on_close)
        while True:

            # 终止信号
            if self.is_stopped:
                plt.show()
                break

            # 如果暂停
            if self.is_continue:
                time.sleep(1)
                continue

            # 如果手动关闭窗口
            if self.is_close:
                return
            # 清除当前坐标轴上的绘图内容，保留其他设置
            plt.cla()
            from classes.yolo import y_axis_count_graph as y
            # from classes.yolo import x_axis_time_graph as x
            plt.xlabel('时间')
            plt.ylabel('车流量/辆')
            plt.title('实时流量折线图')
            plt.plot(y, linestyle='-', marker='o')
            # plt.plot(y, ls='-', marker='o', mec='skyblue', mfc='white', color="skyblue")
            # 发光效果+渐变填充
            mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5, gradient_start='zero')
            plt.xticks([])
            plt.pause(2)


    # 窗口关闭方法
    def on_close(self, event):
        self.is_close = True

    # 停止方法
    def stop(self):
        self.is_stopped = True

    # 暂停方法
    def pause(self):
        self.is_continue = True

    # 继续方法
    def run_continue(self):
        self.is_continue = False

    # 页面关闭方法
    def close_exec(self):
        try:
            self.stop()
            plt.close()
        except Exception as e:
            print(e)
            pass


