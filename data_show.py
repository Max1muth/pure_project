import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

def rasp(data):
    x, y = [], []
    for point in data:
        x += [eval(point)[0]]
        y += [eval(point)[1]]
    return x, y

# fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# ax[0].plot(rasp(df.iloc[0])[0], rasp(df.iloc[0])[1], color="red")
# ax[1].scatter(rasp(df.iloc[0])[0], rasp(df.iloc[0])[1], color="red")

x, y = [], []
for i in range(len(df)):
    x += rasp(df.iloc[i])[0]
    y += rasp(df.iloc[i])[1]

def col(data):
    k = data.shape[1]
    colors_pre = ["red", "orange", "lightgreen", "green", "blue"]
    colors = []
    for i in range(data.shape[0]):
        colors += [colors_pre[i]] * k
    return colors

plt.scatter(x, y, c=col(df))
plt.show()
