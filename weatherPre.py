# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WSjEygOybrtIpHiin48hGfwDjRp72ahB
"""

import pandas as pd
import numpy as np
import pickle
import sys

from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split



def train():

    f = open ("weatherInfo.csv", encoding="CP932")

    data = pd.read_csv(f)

    #天気情報を2値分類
    for i in range(len(data)):
      if data.loc[i,"天気"] == 1 or data.loc[i,"天気"] == 2:
        data.loc[i,"天気"] = 0
      elif data.loc[i,"天気"] == 3 or data.loc[i,"天気"] == 4:
        data.loc[i,"天気"] = 1

    X_data = data[['気温(℃)','現地気圧(hPa)','相対湿度(％)']]
    Y_data = data['天気']

    X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size = 0.2)
    clf = LR()
    clf.fit(X_train.values, y_train)

    with open('model.pickle', mode='wb') as f:
      pickle.dump(clf,f,protocol=2)

    clf.predict(X_test)
    clf.score(X_test, y_test)

def decode():


    with open('model.pickle', mode='rb') as f:
      clf = pickle.load(f)


    #ここに天気情報を入力してください
    #weather = [[11.35, 1009.73, 53.74]]
    temperature = 11.35 #温度情報入力
    humidity = 1009.73 #湿度情報入力
    atmospheric_pressure = 53.74 #気圧情報入力

    weather = [[temperature, atmospheric_pressure, humidity]]

    ans = clf.predict(weather)

    print(ans)


if __name__ == "__main__":

  args = sys.argv
  if args[1] == 'train':
    train()
  else:
    decode()