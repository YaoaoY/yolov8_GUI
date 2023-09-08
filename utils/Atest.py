from datetime import datetime
from pprint import pprint

data = [
    {
        'avatar': 'https://img.kancloud.cn/93/91/9391e3f7266e5d3b79a048512ff9153b_639x640.jpg',
        'create_time': datetime(2023, 7, 31, 17, 27, 34),
        'email': '296711867@qq.com',
        'grade': '超级管理员',
        'id': 1,
        'username': 'pan'
    },
    {
        'avatar': 'https://img.kancloud.cn/93/91/9391e3f7266e5d3b79a048512ff9153b_639x640.jpg',
        'create_time': datetime(2023, 7, 31, 17, 27, 34),
        'email': 'another@example.com',
        'grade': '普通用户',
        'id': 2,
        'username': 'user2'
    }
]

user_dict = {item['id']: item for item in data}

print(user_dict)