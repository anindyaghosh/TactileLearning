import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('sandpaper_C120.csv').to_numpy()
splits = np.array_split(data, np.where(data[:,2] == 10)[0])[1:]

vals = np.arange(4, 20)
for split in splits:
    fig, axes = plt.subplots(figsize=(12, 10), dpi=500)
    for v, val in enumerate(vals):
        axes.plot(split[:,0], split[:,val], label=f'p{v+1}')
    plt.legend()