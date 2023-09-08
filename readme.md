# ✨基于YOLOv8🚀的多端车流检测系统-MTAS (Multi-Platform Traffic Analysis System)

## ⚒️1、客户端环境配置

🚀**第一步 配置python环境**
> - 下载python（版本：python>=3.8）(建议使用访问Anaconda官网配置虚拟环境，具体步骤如下)
>
> - 1）访问Anaconda官网：https://www.anaconda.com/products/individual
>   2）选择相应的操作系统版本并下载对应的安装包（推荐下载64位版本）
>   3）打开下载的安装包，按照提示进行安装即可
>   4）创建一个虚拟环境：
>   
>   ~~~
>   conda create --name 自命名 python=3.9.16
>   ~~~

🚀 **第二步 下载库**
> **注意：下载库前，如果想要更好的帧数体验请安装cuda版本哦(因为一般默认会安装cpu的版本)**
>
> - pip换源：
>
> - ~~~
>   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
>   ~~~
>
> - 切换到项目文件夹下，下载依赖：
>
> - ~~~
>   pip install -r requirements.txt
>   ~~~
>
> - 我自己使用的环境：`python3.9+CPU`

🚀 **第三步 运行项目（如果不需要（开启网页端） 或 （对接RTSP））**

> - 可直接运行项目：python main.py
>
> 🚀**如果需要使用RTSP：**
>
> - 推荐手机安装app——`IP摄像头`
>
> 🚀**如果需要使用网页端：**
>
> - 可参考下面的配置说明


## ⚒️2、配置前端环境（使用网页端）

>🚀**第一步 配置npm与下载依赖**
>
>- 下载node.js（我使用的是16.4版本的）
>
>- npm换源：
>
>- ~~~
>  npm install -g cnpm --registry=https://registry.npm.taobao.org
> 
>- 切换到项目文件夹下，下载依赖：
>
>- ~~~
> npm install
> 
> 🚀**第二步 运行前端**
>
>- ~~~
> npm run dev

## ⭐️3、基本功能

> 👉**系统可大体分为两大模块（客户端、网页端）**

### 客户端 （pyside6+yolov8+pytorch）

> 1. **可接受`多方视频数据流`进行车流分析（调用RTSP摄像头、本地摄像头、上传本地视频）**
> 2. **可对车辆进行`单目追踪`**
> 3. **可`动态调节检测参数`（交互比、置信度、延时、报警阈值）**
> 4. **检测的视频和数据可`保存在本地`**

### 网页端（Vue3+Typestript+Python3+MySQL）

> 1. **多模式分析（用户上传+摄像头拍摄）**
> 2. **数据保存在数据库中（用户数据+检测数据）**
> 3. **可查看触发的警报记录**

### 创新点（毕设需要）

> 1. 结合了**客户端+网页端**（可多端操作）
> 2. 可**动态调整**检测参数（交互比、置信度、延时、报警阈值）
> 3. 可检测出**是否超出车流阈值**（可对接报警模块）
> 4. 检测可通过**多种方式进行（视频流 / 照片）**
> 5. 系统等数据可进行保存（本地文件 / 数据库）
> 6. 可视化车流（光流绘制）显示、可进行**单目追踪、多目标跟踪**（使用集成在yolov8中的bytetrack）
> 7. 车流量可**数据可视化**（动态显示车流量）



## 📚4、使用开源项目+自定义功能借鉴

### 开源项目

>  💎**客户端：https://github.com/CatfishW/MOT & https://github.com/Jai-wei/YOLOv8-PySide6-GUI**

>  💎**前后端：https://github.com/Dovahkiin-Ming/Personnel-Flow-Monitoring-System-based-on-YoloV5**

> 💎 **摄像头视频流直接在浏览器播放：https://www.bilibili.com/video/BV1QM411s77Y**

>  💎**开源视频行为分析系统，系统实现了实时分析视频流，实时产生报警视频，实时推流：https://www.bilibili.com/video/BV1dG4y1k77o**

> 💎**前端：风神的博客（链接未找到）**

### 自定义功能借鉴

> 👍**动态车流量图美化：https://zhuanlan.zhihu.com/p/624890496**

> 👍**网页端摄像头拍照：https://huaweicloud.csdn.net/638f12c7dacf622b8df8e8ee.html**

> 👍**网页端拉取多个视频流：（http-mp4，http-flv等，这种基于http传输，最多只支持6个；本项目采用ws-mp4，即可实现多个分屏）**

> **ps：链接写的不全，总之，衷心感谢大佬们的开源**🌹🌹🌹

## ▶️演示视频与说明

> 🎥演示视频：暂无
>
> 🏠 B站主页：https://space.bilibili.com/279540198
>
> 🔖CSDN：https://blog.csdn.net/Pan_peter
>
> 📌更多毕设：https://www.kancloud.cn/pan123456/web_count/3182391
>
> 

## 📝其他

> - 本项目后面可能要对接数据库，后面再修改就比较麻烦了📦
>
> 🔰**系统方面的拓展：**
>
> - 商场人流检测 🏃
> - 道路路障检测 🚧
> - 疲劳驾驶检测 🚖
>
> 🔔**系统的问题： **
>
> - 部署问题（fps、cuda、onnx）
> - 调用摄像头后无法释放控制权
> - 单目标追踪（开启与关闭）
> - 用户交互
> - 未对接报警模块（比如：加语音提示 or 邮件 or 数据库记录）
> - 未加入数据分析（比如：收集每天时间段，各种车辆的流量，分析出哪些时间段，哪种车型的流量比较大）
> - 拉流存在延迟

