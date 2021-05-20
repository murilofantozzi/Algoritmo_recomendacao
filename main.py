import numpy as np
import pandas as pd

#leitura dos dados
dados = pd.read_csv('dados.csv')
#print(dados)

#separando as categorias e quantidade
grupo = dados.groupby(['categoria']).count()
#print(grupo)

#separando produtos
prod = dados.groupby(['produto']).sum()
#print(prod)

#separando valores
valor = [5]
filtro = dados[dados.categoria.isin(valor)].count()
#print(filtro)

#função para retirar quantidade que uma categoria aparece.
id = [5]
qntd = dados['categoria'].isin(id).sum()
#print(qntd)

#imprime separado por categoria e qtde
id = [3]
qntd = dados['categoria'].isin(id).sum()
freq1 = dados.groupby(['categoria', 'produto']).size()
print(freq1)

#função para contar produto especifico
id = ['Coca cola 600ml']
qntd1 = dados['produto'].isin(id).sum()
#print(qntd1)

soma = qntd1 / qntd
#print(soma)

#busca por cpf
id = ['109.861.250-75']
indice = dados['cpf'].isin(id).sum()
#print(indice)

#quantas vezes comprou de cada categoria
freq = dados.groupby(['cpf', 'categoria']).size()
#print(freq)

maior = freq.max()
#print(maior)

