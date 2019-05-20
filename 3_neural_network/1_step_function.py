import numpy as np
import matplotlib.pylib as plt

# ----------ステップ関数の実装----------

#　 def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# ----------ステップ関数の改良----------
def step_function(x):
    y = x > 0
    return y.astype(np.int)
# print(step_function(np.array([3.0, 2.0, -1.0])))