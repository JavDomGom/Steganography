import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('data.csv', delimiter=',', encoding='utf-8')

for i in dataset.itertuples():
    x = dataset.at[i.Index, 'x']
    y = dataset.at[i.Index, 'y']
    s = dataset.at[i.Index, 's']
    plt.scatter(x, y, s=s, color='black')

plt.title('Point of view')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
