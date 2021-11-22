#!/anaconda3/envs/FEALPy/bin python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: simple_nn.py
# @Author: Jialong Xu
# @Time: 11月 22, 2021
# ---

from keras import models,layers

def simple_nn():
    model = models.Sequential()
    model.add(layers.Dense(16, activation="relu", input_shape=(8000, )))
    model.add(layers.Dropout(.2))
    model.add(layers.Dense(16, activation="relu"))
    model.add(layers.Dropout(.2))
    model.add(layers.Dense(1, activation="sigmoid"))

    model.compile(optimizer="Adam", loss="binary_crossentropy", metrics=["accuracy"])

    return model

model = simple_nn()
model.summary()