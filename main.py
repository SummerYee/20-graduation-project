# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/3/21 1:45
# @File    : 20-graduation-project main.py
# @Software: PyCharm

from test import query_label

while True:
    your_query_sentence = input()
    print('-' * 10)
    label = query_label(your_query_sentence)
    print('predict label:\t', label)
    print('-' * 10)
    if your_query_sentence == '0':
        break


