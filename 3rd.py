import matplotlib.pyplot as plt
import numpy as np

laptops = ["HP", "Asus", "Lenovo", "Apple", "Samsung", "Huawei", "Acer"]
costs = [58, 120, 93, 153, 72, 45, 104]
plt.bar(laptops, costs)
plt.title("Ноутбуки")
plt.xlabel("Ноутбуки")
plt.ylabel("Цена")
plt.show()