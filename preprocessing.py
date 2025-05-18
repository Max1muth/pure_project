import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.ensemble import GradientBoostingClassifier


df = pd.read_csv("df.csv")

print(df.info())

m1 = LabelEncoder()
target_encoded = m1.fit_transform(df["target"])

print(target_encoded)

df["target_en"] = target_encoded
df = df.drop("target", axis=1)

print(df)

scaler = StandardScaler()

scaled_x, scaled_y = scaler.fit_transform(df[["x_c"]]), scaler.fit_transform(df[["y_c"]]) # не знаю почему, но оно с ординарными квадратными - ошибка

print(scaled_x, scaled_y)

df[["x_c"]], df[["y_c"]] = scaled_x, scaled_y
print(df)


colors1 = [(232, 49, 0), (255, 105, 51), (255, 165, 112), (250, 208, 116), (252, 196, 73)]
colors_normalized = [(r/255, g/255, b/255) for r, g, b in colors1]

k = len(df[df["target_en"] == 0])
print(f"k -------------------------------------{k}")
i = int(len(df)/k)
print(f"i ------------------------------------ {i}")
for h in range(i):
    plt.scatter(df.iloc[h*(k+1):(h+1)*(k+1), 0], df.iloc[h*(k+1):(h+1)*(k+1), 1], color=colors_normalized[h])
    plt.show()


x1, y1 = df[["x_c", "y_c"]], df[["target_en"]].values.ravel() # можно убрать и увидеть ошибку,в общем оно приводит в нужный вид

X_train, X_test, y_train, y_test = train_test_split(
    x1, y1, test_size=0.3, random_state=42
)

restrored_y = scaler.inverse_transform(scaled_y) # а на x ошибется - потому что применялся scaler последний раз на y
print(restrored_y)

model = RandomForestClassifier(n_estimators=1, random_state=21)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
mse = mean_squared_error(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"MSE: {mse}, accuracy: {accuracy}")

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
mse = mean_squared_error(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"MSE: {mse}, accuracy: {accuracy}")


gb = GradientBoostingClassifier(n_estimators=100)
gb.fit(X_train, y_train)

y_pred = gb.predict(X_test)
print(y_pred)
print(y_test)
mse = mean_squared_error(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"MSE: {mse}, accuracy: {accuracy}")

