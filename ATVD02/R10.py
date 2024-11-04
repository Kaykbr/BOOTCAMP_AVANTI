import pandas as pd
import numpy as np

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [25, np.nan, 30, 22],
    'Cidade': ['São Paulo', 'Rio de Janeiro', np.nan, 'Belo Horizonte']
}
df = pd.DataFrame(dados)
print("DataFrame Original:")
print(df)

print("\nValores Ausentes:")
print(df.isna())

df_sem_na = df.dropna()
print("\nDataFrame sem valores ausentes:")
print(df_sem_na)

df_preenchido = df.fillna({'Idade': 0, 'Cidade': 'Desconhecida'})
print("\nDataFrame com valores ausentes preenchidos:")
print(df_preenchido)
