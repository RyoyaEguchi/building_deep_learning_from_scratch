import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

def cross_entorpy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size
    return -np.sum(t * np.log(y + delta))

def cross_entorpy_error(y, t):
    if y.ndim = 1:
        t = reshape(1, t.size)
        y = reshape(1, y.size)
    
    batch_size = y.shape[0]


(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(np.random.choice(train_size, batch_size))