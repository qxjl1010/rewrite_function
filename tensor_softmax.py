#!/anaconda3/envs/FEALPy/bin python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: tensor_softmax.py
# @Author: Jialong Xu
# @Time: 11月 19, 2021
# ---

import tensorflow as tf

input_tensor = tf.constant([[1,2,3], [4,5,6]])

max_v = tf.reduce_max(input_tensor, axis=[1])
print(max_v)