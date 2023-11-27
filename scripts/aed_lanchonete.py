#!/usr/bin/env python
# coding: utf-8

# # Importando bibliotecas necessárias

# In[116]:


import openpyxl
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# # Carregando o conjunto de dados do Excel

# In[145]:


df = pd.read_excel('vendas_lanchonete2.xlsx')
df = df[['Produto','Quantidade', 'Valor Total', 'Custo Total', 'Lucro Total', 'Custo Unidade']]


# # Filtrando o DataFrame para manter apenas as colunas relevantes

# In[118]:


df2 = df[['Produto','Quantidade', 'Custo Total', 'Lucro Total']]


# # Exibindo os primeiros registros do DataFrame

# In[119]:


print("### DataFrame Inicial ###")
print(df2)


# # Criando gráficos dos Top 5 produtos em termos de quantidade, Lucro total e valor total
# 

# ### Top 5 produtos mais vendidos

# In[120]:


top5produtos = df.sort_values(by='Quantidade', ascending=False).head(5)
print("\n### Top 5 Produtos Mais Vendidos ###\n")
print(top5produtos)


# ### Top 5 produtos maior faturamento

# In[133]:


top5faturamento = df.sort_values(by='Valor Total', ascending=False).head(5)
print("\n### Top 5 Produtos Maior Faturamento ###\n")
print(top5vendas)


# ### Top 5 produtos mais lucrativos

# In[134]:


top5vendas = df.sort_values(by='Lucro Total', ascending=False).head(5)
print("\n### Top 5 Produtos Mais Lucrativos ###\n")
print(top5vendas)


# # Criando gráficos de barras para os Top 5 produtos

# In[136]:


plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.title('Top 5 Produtos Mais Vendidos')
sns.barplot(x='Produto', y='Quantidade', data=top5produtos)
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
plt.title('Top 5 Produtos Maior Faturamento')
sns.barplot(x='Produto', y='Valor Total', data=top5vendas)
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
plt.title('Top 5 Produtos Mais Lucrativos')
sns.barplot(x='Produto', y='Lucro Total', data=top5vendas)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# # Estatísticas descritivas do conjunto de dados

# In[150]:


estatisticas = df.describe()
print("\n### Estatísticas Descritivas ###\n")
print(estatisticas)


# # Criando boxplots para 'Quantidade' e 'Valor Total'

# In[148]:


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Boxplot Quantidade')
plt.boxplot(df['Quantidade'])

plt.subplot(2, 2, 2)
plt.title('Lucro Total')
plt.boxplot(df['Lucro Total'])

plt.subplot(2, 2, 3)
plt.title('Valor Faturado')
plt.boxplot(df['Valor Total'])

plt.subplot(2, 2, 4)
plt.title('Custo Unidade')
plt.boxplot(df['Custo Unidade'])


plt.tight_layout()
plt.show()



# # Criando um gráfico de dispersão entre 'Quantidade' e 'Valor Total'

# In[149]:


plt.figure(figsize=(12, 4))

sns.lmplot(x='Quantidade', y='Valor Total', data=df)
plt.xlabel('Quantidade')
plt.ylabel('Valor Total')
plt.title('Gráfico de Dispersão')
plt.show()


# In[ ]:




