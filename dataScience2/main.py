import pandas as pd
import numpy as np

data = pd.read_csv("Pokemon.csv")

print(data.head())
print(data.columns)
print(data.HP.mean())
print(data.HP.max())
print("--------")
print(data.Attack.max())
print("--------")
print(data[data["Attack"]==190]["Type 1"])
data.drop(["Name"],axis=1,inplace=True)
print("--------")

list=['Total', 'HP', 'Attack', 'Defense',
       'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
result=data.groupby('Type 1')[list].min()

print(data["Type 1"].value_counts())