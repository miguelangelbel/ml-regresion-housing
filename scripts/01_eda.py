import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from src.data import read_raw_data
from src.transform import prepare_data

# Read the csv and create the pandas dataframe
df_raw = read_raw_data()

df_processed = prepare_data(df_raw)

print(df_processed.head(10))
print(len(df_raw))
print(len(df_processed))
print("\n")
p = sns.displot(data=df_raw, x="price")
p.fig.suptitle("Distribución de precios de vivienda")
p.fig.tight_layout()
plt.show()

m = sns.displot(data=df_raw, x="m2")
m.fig.suptitle("Distribución de m2 de vivienda")
m.fig.tight_layout()
plt.show()
