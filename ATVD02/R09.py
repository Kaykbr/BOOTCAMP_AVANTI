import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('ATVD02\GlobalLandTemperaturesByCountry.csv')

coluna_AVGtemp = df['AverageTemperature']
print(coluna_AVGtemp)

# Filtrar linhas onde a avg temp é maior que 4
filtro = df[df['AverageTemperature'] > 4]
print(filtro)
