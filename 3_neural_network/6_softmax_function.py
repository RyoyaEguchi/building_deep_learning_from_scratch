import numpy as np
import matplotlib.pylab as plt

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_a = np.sum(exp_a)
    print(exp_a)
    print(sum_a)
    y = exp_a / sum_a
    
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))