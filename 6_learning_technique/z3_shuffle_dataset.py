import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist()

# 検証データをシャッフル
# shuffle_datasetは、np.random.shuffleを利用した関数。common/util.pyにあり。
x_train, t_train = shuffle_dataset(x_train, t_train) 

# 検証データの分割
validation_rate = 0.20
validation_num = int(x_train.shape[0] * validation_rate)

x_val = x_train[:validation_num]
t_val = t_train[:validation_num]
x_train = x_train[validation_num:]
t_train = t_train[validation_num:]

