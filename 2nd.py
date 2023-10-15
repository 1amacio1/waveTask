import matplotlib.pyplot as plt
import numpy as np


plt.figure('Графики', figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.title('Функция y = cos(x)')
x1 = np.linspace(-2 * np.pi, 2 * np.pi, 240)
y1 = np.cos(x1)
plt.plot(x1, y1, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 2)
plt.title('Функция y = sin(x)')
y2 = np.sin(x1)
plt.plot(x1, y2, color='red')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 3)
plt.title('Функция y = x^2')
x3 = np.linspace(-8, 8, 100)
y3 = x3 ** 2
plt.plot(x3, y3, color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 4)
plt.title('Функция y = 2/x')
x4_1 = np.linspace(-2, -0.01, 100)
x4_2 = np.linspace(0.01, 2, 100)
y4_1 = 2 / x4_1
y4_2 = 2 / x4_2
plt.plot(x4_1, y4_1,  x4_2, y4_2, color='brown')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()