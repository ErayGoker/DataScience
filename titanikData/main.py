import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

pd.set_option('display.max_columns', None)
print(train.to_string())
print(train.describe().to_string())
print(train.info())

def degiskenler(variable):
    cat=train[variable]
    sayi=cat.value_counts()
    plt.figure(figsize=(9,3))
    plt.bar(sayi.index,sayi)
    plt.xticks(sayi.index,sayi.index.values)
    plt.ylabel("Frekans")
    plt.title(variable)
    plt.show()
    print(variable,sayi)

category=[ 'Survived', 'Pclass', 'Name', 'Sex','SibSp','Embarked','Parch']

#for i in category:
#    degiskenler(i)