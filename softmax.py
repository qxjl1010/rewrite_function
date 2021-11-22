#!/anaconda3/envs/FEALPy/bin python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: tensor_softmax.py
# @Author: Jialong Xu
# @Time: 11月 19, 2021
# ---

import math


def softmax(input_vec):
    output_vec = []

    sum = 0

    max_v = max(input_vec)

    for i in input_vec:
        sum += math.exp(i-max_v)

    for i in input_vec:
        output_vec.append(math.exp(i-max_v)/sum)

    return output_vec

if __name__ == '__main__':
    print(softmax([2,3,4]))