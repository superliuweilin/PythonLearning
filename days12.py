# 例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息。
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


# def main():
#     username = input('请输入用户名：')
#     qq = input('请输入QQ号：')
#     # match函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#     # 5~12的数字
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m1:
#         print('请输入有效的用户名')
#     if not m2:
#         print('请输入正确的QQ号')
#     if m1 and m2:
#         print('你输入的信息是有效的！')

# 从一段文字中提取国内的手机号码
def main():
    # 创建正则表达式 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    # 查找所有匹配并保存到一个列表中
    my_list = re.findall(pattern, sentence)
    print(my_list)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(type(temp))
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    # print(m.end())
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())




if __name__ == '__main__':
    main()
