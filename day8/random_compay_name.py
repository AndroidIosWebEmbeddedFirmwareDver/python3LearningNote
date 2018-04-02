# TODO
import random

li = ['宾果', '宾够', '博纳', '陌陌', '拉钩',
      '博汇', '聚设计', '超纳', '微纳', '阿里巴巴',
      '人人设计',
      '天天设计',
      '汇聚',
      '腾讯']


# li=[
#     '博',
#     '纳',
#     '聚',
#     '微',
#     '阿',
#     '一',
#     '爱',
# ]


def gener(dec, length):
    """"""
    result = ''
    try:
        for i in range(0, length):
            result += dec[random.randint(0, len(dec) - 1)]
    except Exception as e:
        print(e)
    return result


def split():
    """"""
    result = []
    for x in li:
        # print(x)
        for y in x:
            # print(y)
            result.append(y)
    return result


# 生成随机中文字符
def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


if __name__ == '__main__':
    # print(split())
    for x in range(0, 20):
        # print(gener(split(), 2) + '设计')
        print(GBK2312() + GBK2312() + '设计')
    # for x in range(0, 10):
    #     print(gener(split(), 3))
    # for x in range(0, 100):
    #     print(gener(split(), 2))
