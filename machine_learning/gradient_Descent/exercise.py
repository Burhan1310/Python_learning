import math

import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0001

    cost_previous = 0

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print("m {}, b {}, cost {}, iterations {}".format(m_curr, b_curr, cost, i))


x = np.array([92, 56, 88, 70, 80, 49, 65, 35, 66, 67])
y = np.array([98, 68, 81, 80, 83, 52, 66, 30, 68, 73])

gradient_descent(x, y)
