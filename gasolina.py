
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv', delimiter=',', encoding='utf8')
data = sns.lineplot(x='dia', y='venda', data=df, color='red')
data.set(title='Price of a Liter of Gasoline', xlabel='Days', ylabel='Price')
plt.savefig('gasolina.png')
  