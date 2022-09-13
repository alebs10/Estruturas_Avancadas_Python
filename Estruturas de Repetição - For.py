#!/usr/bin/env python
# coding: utf-8

# In[1]:


#UTILIZANDO FOR

nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']

for nome in nomes_cidades:
    print(nome)


# In[4]:


#UTILIZANDO WHILE

contador = 0

nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador = contador + 1


# In[5]:


#TRABALHANDO COM TUPLA

nomes_cidades = 'São Paulo', 'Londres', 'Tóquio', 'Paris'
for nome in nomes_cidades:
    print(nome)


# In[6]:


cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao': 12.2
}

for chave in cidade:
    print(f'{chave} : {cidade[chave]}')


# In[8]:


nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']

for nome in nomes_cidades:
    nome = 'Rio de Janeiro'
    
print(nomes_cidades)


# In[10]:


#RANGE CRIA UM OBJETO COMO UMA LISTA QUE CONTÉM ELEMENTOS DE 0
# ATÉ O LIMITANTE PARA A FUNÇÃO -1

for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de Janeiro'
    
print(nomes_cidades)


# In[13]:


print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))


# In[ ]:




