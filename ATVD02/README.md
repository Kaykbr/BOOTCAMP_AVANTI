# Atividades de Programação em Python

Este projeto contém as soluções para as **Atividades 1 a 10** propostas, abordando diversos conceitos de programação em Python, incluindo manipulação de listas, funções matemáticas, visualização de dados com Matplotlib, e análise de dados com Pandas.

## **Sumário das Atividades**

1. **Atividade 1:** Filtrar números ímpares de uma lista.
2. **Atividade 2:** Filtrar números primos de uma lista.
3. **Atividade 3:** Encontrar elementos exclusivos entre duas listas.
4. **Atividade 4:** Encontrar o segundo maior valor em uma lista.
5. **Atividade 5:** Ordenar uma lista de tuplas pelo nome em ordem alfabética.
6. **Atividade 6:** Criar subplots com anotações usando Matplotlib.
7. **Atividade 7:** Plotar a função seno usando Numpy e Matplotlib.
8. **Atividade 8:** Ler um arquivo CSV com Pandas e exibir as primeiras linhas.
9. **Atividade 9:** Selecionar uma coluna específica e filtrar linhas com base em uma condição usando Pandas.
10. **Atividade 10:** Tratar valores ausentes (`NaN`) em um DataFrame com Pandas.

## **Detalhes das Atividades com Explicação**

### **Atividade 6: Criar Subplots com Anotações usando Matplotlib**

Este código utiliza a biblioteca `matplotlib` para criar uma figura contendo quatro subplots organizados em uma grade de 2x2. Cada subplot é anotado no centro para indicar sua posição na grade.

**Componentes Principais:**

- **Importações:**
  - `matplotlib.pyplot` como `plt` para funcionalidades de plotagem.
  - `numpy` como `np` para operações numéricas (não utilizado diretamente nesta atividade, mas importado para possíveis extensões).

- **Criação de Subplots:**
  - `plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), constrained_layout=True)` cria uma figura com 2 colunas e 2 linhas de subplots.

- **Anotações:**
  - Dois loops `for` iteram sobre as linhas (`row`) e colunas (`col`) para adicionar uma anotação no centro de cada subplot indicando sua posição, por exemplo, `axs[0, 0]`.

- **Título da Figura:**
  - `fig.suptitle('plt.subplots()')` adiciona um título geral para a figura.

- **Exibição:**
  - `plt.show()` exibe a figura com os subplots anotados.

**Output Esperado:**

Uma janela gráfica exibindo quatro subplots, cada um com uma anotação indicando sua posição (e.g., `axs[0, 0]`, `axs[0, 1]`, etc.) e o título "plt.subplots()".

### **Atividade 7: Plotar a Função Seno usando Numpy e Matplotlib**

Este código gera e plota a função seno utilizando as bibliotecas `numpy` para gerar os dados e `matplotlib` para visualização.

**Componentes Principais:**

- **Importações:**
  - `numpy` como `np` para gerar uma sequência de valores.
  - `matplotlib.pyplot` como `plt` para criar o gráfico.

- **Geração de Dados:**
  - `np.linspace(-2 * np.pi, 2 * np.pi, 100)` gera 100 pontos igualmente espaçados entre `-2π` e `2π`.
  - `np.sin(x)` calcula o seno de cada ponto em `x`.

- **Plotagem:**
  - `plt.subplots()` cria uma figura e um eixo (`ax`).
  - `ax.plot(x, y)` plota a função seno.
  - `ax.set_title('Gráfico de Seno')` adiciona um título ao gráfico.

- **Exibição:**
  - `plt.show()` exibe o gráfico da função seno.

**Output Esperado:**

Um gráfico da função seno variando de `-2π` a `2π` com o título "Gráfico de Seno".

### **Atividade 8: Ler um Arquivo CSV com Pandas e Exibir as Primeiras Linhas**

Este código utiliza a biblioteca `pandas` para ler dados de um arquivo CSV e exibir as primeiras linhas do DataFrame resultante.

**Componentes Principais:**

- **Importação:**
  - `pandas` como `pd` para manipulação de dados.

- **Leitura do CSV:**
  - `pd.read_csv('caminho/para/arquivo.csv')` lê o arquivo CSV e armazena os dados em um DataFrame chamado `df`.

- **Exibição:**
  - `df.head()` exibe as primeiras 5 linhas do DataFrame por padrão.

**Como Usar:**

1. Substitua `'caminho/para/arquivo.csv'` pelo caminho real do seu arquivo CSV.
2. Execute o script para visualizar as primeiras linhas do seu conjunto de dados.

**Output Esperado:**

As primeiras 5 linhas do arquivo CSV exibidas no console, permitindo uma rápida visualização dos dados.

### **Atividade 9: Selecionar uma Coluna e Filtrar Linhas com Base em uma Condição usando Pandas**

Este código demonstra como selecionar uma coluna específica de um DataFrame e filtrar as linhas com base em uma condição definida.

**Componentes Principais:**

- **Leitura do CSV:**
  - `pd.read_csv('caminho/para/arquivo.csv')` lê o arquivo CSV e armazena os dados em `df`.

- **Seleção de Coluna:**
  - `df['Idade']` seleciona a coluna intitulada `'Idade'`.

- **Filtragem de Linhas:**
  - `df[df['Idade'] > 30]` filtra as linhas onde o valor na coluna `'Idade'` é maior que 30.

**Como Usar:**

1. Substitua `'caminho/para/arquivo.csv'` pelo caminho real do seu arquivo CSV.
2. Execute o script para visualizar a coluna `'Idade'` e as linhas onde `'Idade'` é maior que 30.

**Output Esperado:**

- **Coluna Selecionada:** Exibição de todos os valores na coluna `'Idade'`.
- **Linhas Filtradas:** Exibição das linhas onde a `'Idade'` é maior que 30.

### **Atividade 10: Tratar Valores Ausentes (`NaN`) em um DataFrame com Pandas**

Este código demonstra diferentes métodos para lidar com valores ausentes (`NaN`) em um DataFrame utilizando a biblioteca `pandas`.

**Componentes Principais:**

- **Importações:**
  - `pandas` como `pd` para manipulação de dados.
  - `numpy` como `np` para representar valores ausentes (`NaN`).

- **Criação do DataFrame:**
  - Um DataFrame é criado com algumas entradas `NaN` nas colunas `'Idade'` e `'Cidade'`.

- **Verificação de Valores Ausentes:**
  - `df.isna()` retorna um DataFrame booleano indicando onde estão os valores ausentes.

- **Remoção de Linhas com `NaN`:**
  - `df.dropna()` remove todas as linhas que contêm pelo menos um valor ausente.

- **Preenchimento de Valores Ausentes:**
  - `df.fillna({'Idade': 0, 'Cidade': 'Desconhecida'})` substitui os valores ausentes na coluna `'Idade'` por `0` e na coluna `'Cidade'` por `'Desconhecida'`.

**Como Usar:**

1. Execute o script para ver como o DataFrame original, a verificação de `NaN`, a remoção de linhas com `NaN`, e o preenchimento de valores ausentes são realizados.
2. Observe as diferentes saídas no console para entender o impacto de cada operação.

**Output Esperado:**

- **DataFrame Original:** Exibição do DataFrame com valores ausentes (`NaN`).
- **Valores Ausentes:** Indicação de onde estão os `NaN` no DataFrame.
- **DataFrame sem valores ausentes:** Exibição do DataFrame após a remoção das linhas com `NaN`.
- **DataFrame com valores ausentes preenchidos:** Exibição do DataFrame após o preenchimento dos valores ausentes com os valores especificados.

## **Como Executar os Códigos**

1. **Pré-requisitos:**
   - **Python 3.x** instalado na sua máquina.
   - Bibliotecas necessárias: `matplotlib`, `numpy`, e `pandas`. Você pode instalá-las usando `pip`:
     ```bash
     pip install matplotlib numpy pandas
     ```

2. **Estrutura do Projeto:**
   - Crie um arquivo Python, por exemplo, `atividades.py`, e copie todo o código fornecido acima para esse arquivo.
   - Certifique-se de ter os arquivos CSV necessários para as atividades 8, 9 e 10, ou ajuste os caminhos conforme necessário.

3. **Executar o Script:**
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `atividades.py` está localizado.
   - Execute o script:
     ```bash
     python atividades.py
     ```

4. **Observações:**
   - As atividades que envolvem gráficos (`Atividades 6 e 7`) abrirão janelas de visualização gráfica.
   - As atividades que envolvem leitura de CSV (`Atividades 8, 9 e 10`) requerem que você substitua `'caminho/para/arquivo.csv'` pelo caminho real do seu arquivo CSV.

## **Conclusão**

Este projeto abrange uma variedade de conceitos fundamentais em Python, desde manipulação básica de listas até visualização e análise de dados mais avançadas com `matplotlib` e `pandas`. Sinta-se à vontade para explorar e modificar os códigos conforme necessário para aprofundar seu entendimento.

Se tiver dúvidas ou precisar de mais explicações, não hesite em procurar recursos adicionais ou perguntar a colegas e instrutores.

---
