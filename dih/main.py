#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:35:16 2018

@author: jayesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime



df = pd.read_excel('list.xlsx')
df = df.T
header = df.iloc[1]
df = df.iloc[2:]
df = df.rename(columns = header)
df = df.iloc[:,0:1]
'''xf = df.iloc[:,2:]
yf = xf
for i in range(len(xf)):
plt.plot(y_test)
plt.plot(y_pred)
plt.legend(['Actual Quantity','Predicted Quantity'])
plt.show()

    y = xf.iloc[i:i+1,:]
    x = np.random.uniform(size=y.size)
    yf.iloc[i:i+1,:] = y + (x-0.5)*(np.mean(y)/20)
yf = yf*100
yf = np.around(yf)
yf = yf/100
yf.to_excel('listii.xlsx')
'''

split_date = datetime.datetime(2017, 12, 1, 18, 00)
train = df[df.index < split_date]
test = df[df.index > split_date]


plt.plot(train)
plt.plot(test)
plt.legend(['train','test'])



from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)

X_train = train_sc[:-1]
y_train = train_sc[1:]

X_test = test_sc[:-1]
y_test = test_sc[1:]

m,n = X_train.shape
X_train = np.reshape(X_train,(m,n,1))
m,n = X_test.shape
X_test = np.reshape(X_test,(m,n,1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

model = Sequential()
model.add(LSTM(12,input_shape=(None,1),activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')
model.summary()
model.fit(X_train,y_train,epochs=100,batch_size=2,verbose=1)
y_pred = model.predict(X_test)


y_pred = sc.inverse_transform(y_pred)
y_test = pd.DataFrame(sc.inverse_transform(y_test))
import math
from sklearn.metrics import mean_squared_error
rmse = math.sqrt(mean_squared_error(y_test,y_pred))
rms = math.sqrt(mean_squared_error(np.zeros(2),y_test))

'''index = y_test.index
y_test = pd.DataFrame(y_test)
y_test['date']=index
y_pred = pd.DataFrame(y_pred)
y_pred=y_pred.iloc[1:,:]
y_pred=y_pred.reset_index()
y_pred.drop(['index'], axis = 1, inplace = True)
y_pred['date']=index
y_pred = y_pred.set_index('date')
y_test = y_test.set_index('date')'''

plt.plot(y_test)
plt.plot(y_pred)
plt.legend(['Actual Quantity','Predicted Quantity'])
plt.show()


















