import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os

df = pd.read_csv(r"C:\Projects\LearnKaggleTitanic\train.csv")

print(df.isnull().sum().sort_values(ascending=False))

# ใส่ค่า missing ของ Age ด้วย median ของ Age
df["Age"] = df["Age"].fillna(df["Age"].median())

# เปอเซ็นต์ การรอดชีวิต 
print(df["Survived"].value_counts(normalize=True) * 100)

# โอกาสรอดจากเพศ
print(df.groupby("Sex")["Survived"].mean() * 100)

df.groupby("Sex")["Survived"].mean().mul(100).plot(
    kind="bar",
    ylabel="Survival Rate (%)",
    title="Survival Rate by Sex"
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# โอกาสรอดจากชั้นโดยสาร
print(df.groupby("Pclass")["Survived"].mean() * 100)
df.groupby("Pclass")["Survived"].mean().mul(100).plot(
    kind="bar",
    ylabel="Survival Rate (%)",
    xlabel="Passenger Class",
    title="Survival Rate by Passenger Class"
)

plt.tight_layout()
plt.show()


print(df["Age"].mean())