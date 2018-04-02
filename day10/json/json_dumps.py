import json

# 将python direct 转 json
data = {'aaa': 1123123, 'asdasd': '123123'}


def p_direct_to_json_data(data):
    """"""
    return json.dumps(data)


if __name__ == '__main__':
    convert_data = p_direct_to_json_data(data)
    print('PYTHON原始数据：{0}'.format(data))
    print('JSON  转换数据：{0}'.format(convert_data))
