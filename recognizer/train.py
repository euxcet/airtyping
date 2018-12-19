import keras
#from keras.models import Sequential
from keras.layers import Dense
from keras.models import *
import numpy as np
#import matplotlib.pyplot as plt



#model = load_model('model.h5')


model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=18))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=11, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])


f = open("data.out", "r")
x = []
y = []
xx = []
yy = []

lines = f.readlines()

for line in lines:
    data = map(lambda x: float(x), line.split(' '))
    data[0] = int(data[0])
    data[-1] = int(data[-1])
    x.append(data[1:-1])
    y.append(data[-1])
f.close()

ftest = open("test.out", "r")
lines = ftest.readlines()
for line in lines:
    data = map(lambda x: float(x), line.split(' '))
    data[0] = int(data[0])
    data[-1] = int(data[-1])
    xx.append(data[1:-1])
    yy.append(data[-1])



x_train = np.array(x) / 100
y_train = np.array(y)

x_test = np.array(xx) / 100
y_test = np.array(yy)

y_train = keras.utils.to_categorical(y_train, num_classes = 11)
y_test = keras.utils.to_categorical(y_test, num_classes = 11)



print x_train.shape
print y_train.shape

model.fit(x_train, y_train, epochs=60, batch_size=4)
model.save('model.h5')



'''
print x_test.shape
classes = model.predict(x_test, batch_size=128)
print model.predict(x_test, batch_size=128)
for c in classes:
    value = 0
    pos = -1
    for j in xrange(0, 11):
        print c[j], value
        if (c[j] > value):
            value = c[j]
            pos = j
    print pos
'''

