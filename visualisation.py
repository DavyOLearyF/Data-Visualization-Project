import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("my_data.csv")
plt.hist(df)