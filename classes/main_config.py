# -*- coding: utf-8 -*-
# @Author : pan
# @Description : 集成配置（单例模式）
# @Date : 2023年7月26日12:49:37

import json
import os


class MainConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_path="main_config.json"):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        self.config_path = config_path

        # 默认配置
        self.iou = 0.5
        self.conf = 0.5
        self.rate = 1.0
        self.save_res = False
        self.save_txt = False
        self.save_res_path = "pre_result"
        self.save_txt_path = "pre_labels"
        self.models_path = "models"
        self.show_trace = True
        self.show_labels = True
        self.open_fold = os.getcwd()  # 设置为当前工作目录的路径
        self.rtsp_ip = "rtsp://admin:admin@192.168.43.1:8554/live"
        self.car_id = 1
        self.car_threshold = 10
        # 读取配置文件
        self.load_config()

    def load_config(self):
        # 如果文件不存在（写入，然后使用默认值）
        if not os.path.exists(self.config_path):
            self.save_config()
            return
        # 如果文件存在（修改默认值）
        with open(self.config_path) as f:
            try:
                config_data = json.load(f)
                # 读取配置
                self.iou = config_data.get("iou", self.iou)
                self.conf = config_data.get("conf", self.conf)
                self.rate = config_data.get("rate", self.rate)

                self.save_res = config_data.get("save_res", self.save_res)
                self.save_txt = config_data.get("save_txt", self.save_txt)
                self.save_res_path = config_data.get("save_res_path", self.save_res_path)
                self.save_txt_path = config_data.get("save_txt_path", self.save_txt_path)
                self.models_path = config_data.get("models_path", self.models_path)
                self.show_labels = config_data.get("show_labels", self.show_labels)
                self.show_trace = config_data.get("show_trace", self.show_trace)

                self.open_fold = config_data.get("open_fold", self.open_fold)
                self.rtsp_ip = config_data.get("rtsp_ip", self.rtsp_ip)
                self.car_id = config_data.get("car_id", self.car_id)
                self.car_threshold = config_data.get("car_threshold", self.car_threshold)
            except (json.JSONDecodeError, KeyError, TypeError):
                self.save_config()

    # 保存配置
    def save_config(self):
        new_config = {"iou": self.iou,
                      "conf": self.conf,
                      "rate": self.rate,
                      "save_res": self.save_res,
                      "save_txt": self.save_txt,
                      "save_res_path": self.save_res_path,
                      "save_txt_path": self.save_txt_path,
                      "models_path" : self.models_path,
                      "open_fold": self.open_fold,
                      "show_trace": self.show_trace,
                      "show_labels": self.show_labels,
                      "rtsp_ip": self.rtsp_ip,
                      "car_id": self.car_id,
                      "car_threshold": self.car_threshold
                      }
        new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
        with open(self.config_path, 'w', encoding='utf-8') as f:
            f.write(new_json)
        return


if __name__ == "__main__":
    config = MainConfig()