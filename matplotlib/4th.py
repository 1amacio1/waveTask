import matplotlib.pyplot as plt
import numpy as np
import random

def pie(n):
    labels = [i for i in range(n)]
    values = [random.randint(0, 25) for i in range(n)]
    plt.pie(values, labels=labels)
    plt.show()

pie(7)