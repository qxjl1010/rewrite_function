#!/anaconda3/envs/FEALPy/bin python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: sigmoid.py
# @Author: Jialong Xu
# @Time: 11月 22, 2021
# ---

import math

def sigmoid(input_v):
    return 1/(1+math.exp(-input_v))

def tanh(input_v):
    return (math.exp(input_v) - math.exp(-input_v)) / (math.exp(input_v) + math.exp(-input_v))

def relu(input_v):
    return 0 if input_v < 0 else input_v

if __name__ == '__main__':
    print(relu(-2))