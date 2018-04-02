"""

如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：
"""
import json

data = {
    'aaa': 1123123,
    'asdasd': '123123',
    '1': '123123',
    '2': '123123',
    '5': '123123',
    '3': '123123',
    '4': '123123',
    '6': '123123',
}


def dump_json_file(doneFileUrl, data):
    """写入JSON数据到文件"""
    # 写入 JSON 数据
    with open(doneFileUrl, 'w') as f:
        json.dump(data, f)


def load_json_file(doneFileUrl):
    """从文件读出JSON数据"""
    # 读取数据
    with open(doneFileUrl, 'r') as f:
        resultData = json.load(f)
    return resultData


if __name__ == '__main__':
    fileUrl = 'test_json.json'
    dump_json_file(fileUrl, data)
    print(load_json_file(fileUrl))
