import matplotlib.pyplot as plt
import numpy as np

def f(y1="2x+1" , y2="3x-2"):
    x = np.linspace(-5, 5, 100)
    y1 = y1.split("x")
    y2 = y2.split("x")
    if y1[1] != "":
        func1 = [int(y1[0]) * i + int(y1[1]) for i in x]
    else:
        func1 = [int(y1[0]) * i for i in x]
    if y2[1] != "":
        func2 = [int(y2[0]) * i + int(y2[1]) for i in x]
    else:
        func2 = [int(y2[0]) * i for i in x]
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.plot(x, func1, x, func2)
    plt.show()


f()

