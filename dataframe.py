import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
print(data.iloc[:, :])

x_c = []
y_c = []
target = []

for i in range(len(data)):
    for k in range(len(data.columns)):
        print(eval(data.iloc[i, k])) # тут можно, но лучше eval не использовать - может вызвать скрипт
        x_c += [list(eval(data.iloc[i, k]))[0]]
        y_c += [list(eval(data.iloc[i, k]))[1]]
        target += [list(eval(data.iloc[i, k]))[2]]
print(x_c, y_c, target, sep="\n\n")


df = pd.DataFrame(list(zip(x_c, y_c, target)), 
                 columns=['x_c', 'y_c', 'target'])

print(df)
df.to_csv("df.csv", index=False)

g = pd.read_csv("df.csv")

print(g)
plt.figure(figsize=(8, 6))
colors1 = [(232, 49, 0), (255, 105, 51), (255, 165, 112), (250, 208, 116), (252, 196, 73)]
colors_normalized = [(r/255, g/255, b/255) for r, g, b in colors1]

for h in range(i+1):
    plt.scatter(g.iloc[h*(k+1):(h+1)*(k+1), 0], g.iloc[h*(k+1):(h+1)*(k+1), 1], color=colors_normalized[h])
    plt.show()
# plt.scatter(g["x_c"], g["y_c"])
# plt.show()
