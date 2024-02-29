
      import pandas as pd
      import seaborn as sns
      import matplotlib.pyplot as plt

      df = pd.read_csv('gasolina.csv', delimiter=',',encoding='utf8')

      data = sns.lineplot(x='dia', y='venda', data=df)
      data.set(title='Preço do Litro da Gasolina', xlabel='Dias', ylabel='Preço (R$)')
      plt.savefig('gasolina.png')
  