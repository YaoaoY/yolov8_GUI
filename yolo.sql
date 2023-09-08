/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : yolo

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 02/08/2023 16:11:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alarm
-- ----------------------------
DROP TABLE IF EXISTS `alarm`;
CREATE TABLE `alarm`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '警报id',
  `location` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '警报地点',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '警报信息',
  `threshold` int(0) NOT NULL COMMENT '监控阈值',
  `photo` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '照片路径',
  `pid` int(0) NOT NULL COMMENT '监控id',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alarm
-- ----------------------------
INSERT INTO `alarm` VALUES (1, '炳草岗大街', '车流量:17', 10, 'http://127.0.0.1:5500//static/after_img/2023-08-01/2023-08-01-11-31-10_kknqb_alarm.jpg', 1, '2023-08-01 11:31:10', '无');
INSERT INTO `alarm` VALUES (2, '炳草岗大街', '车流量:17', 10, 'http://127.0.0.1:5500//static/after_img/2023-08-01/2023-08-01-11-31-10_zqhxx_alarm.jpg', 1, '2023-08-01 11:31:10', '无');

-- ----------------------------
-- Table structure for monitor
-- ----------------------------
DROP TABLE IF EXISTS `monitor`;
CREATE TABLE `monitor`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '监控id',
  `threshold` int(0) NOT NULL COMMENT '警报阈值',
  `person` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '配置人员',
  `video` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '视频路径',
  `url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '拉流路径',
  `is_alarm` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '警报状态',
  `mode` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '算法模式',
  `location` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '监控地点',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `create_by` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '创建人',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of monitor
-- ----------------------------
INSERT INTO `monitor` VALUES (1, 10, 'Pan', 'ws://127.0.0.1/live/test.live.mp4', 'rtsp://127.0.0.1:554/live/test', '关闭', '快速模式', '炳草岗大街', '2023-07-31 21:41:32', '', '无');
INSERT INTO `monitor` VALUES (2, 40, 'Pan', 'ws://127.0.0.1/live/test.live.mp4', 'rtsp://127.0.0.1:554/live/test', '开启', '快速模式', '贵阳北站', '2023-08-01 17:27:18', '', '好多车');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '密码',
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '邮箱',
  `avatar` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '头像',
  `grade` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `create_by` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '创建人',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'pan', '123456', '296711867@qq.com', 'https://img.kancloud.cn/93/91/9391e3f7266e5d3b79a048512ff9153b_639x640.jpg', '超级管理员', '2023-07-31 17:27:34', 'pan', '菜鸟');

SET FOREIGN_KEY_CHECKS = 1;
