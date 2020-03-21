# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/3/20 23:25
# @File    : 20-graduation-project test.py
# @Software: PyCharm

import pickle
import numpy as np
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
import jieba


# 加载 pickle 对象的函数
def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# 输入模型的最终单句长度
max_cut_query_lenth = 26

# 加载查询词汇和对应 ID 的字典
word_index_dict = load_obj('word_index_dict')
# 加载模型输出 ID 和对应标签（种类）的字典
index_label_dict = load_obj('index_label_dict')
# 加载模型结构
model_json = load_obj('model_json')
model = model_from_json(model_json)
# 加载模型权重
model.load_weights('my_model.h5')


def query_label(query_sentence):
    '''
    input query: "从中山到西安的汽车。"
    return label: "bus"
    '''
    x_input = []
    # 分词 ['从', '中山', '到', '西安', '的', '汽车', '。']
    query_sentence_list = list(jieba.cut(query_sentence))
    # 序列化 [54, 717, 0, 8, 0, 0, 1, 0, 183, 2]
    x = [word_index_dict.get(w, 0) for w in query_sentence]
    # 填充  array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    #      0,   0,   0,  54, 717,   0,   8,   0,   0,   1,   0, 183,   2]], dtype=int32)
    x_input.append(x)
    x_input = pad_sequences(x_input, maxlen=max_cut_query_lenth)
    # 预测
    y_hat = model.predict(x_input)
    # 取最大值所在的序号 11
    pred_y_index = np.argmax(y_hat)
    # 查找序号所对应标签（类别）
    label = index_label_dict[pred_y_index]
    return label


if __name__ == "__main__":
    query_sentence = '听音乐'
    print(query_label(query_sentence))



while True:
    your_query_sentence = input()
    print('-' * 10)
    label = query_label(your_query_sentence)
    print('predict label:\t', label)
    print('-' * 10)
    if your_query_sentence == '0':
        break
