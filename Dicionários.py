#!/usr/bin/env python
# coding: utf-8

# In[1]:


#VERBETES = chaves
#SIGNIFICADOS = valores das chaves

dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.18
}

print(dados_cidade, type(dados_cidade))


# In[2]:


dados_cidade['pais'] = 'Brasil'


# In[3]:


print(dados_cidade)


# In[4]:


print(dados_cidade['nome'])


# In[5]:


dados_cidade['area_km2'] = 1500
print(dados_cidade)


# In[6]:


#COPY

dados_cidade2 = dados_cidade


# In[7]:


dados_cidade2['nome'] = 'Santos'


# In[8]:


print(dados_cidade2)


# In[9]:


dados_cidade3 = dados_cidade.copy()


# In[10]:


dados_cidade3['estado'] = 'Rio de Janeiro'


# In[11]:


print(dados_cidade3)


# In[12]:


print(dados_cidade)


# In[13]:


#UPDATE

novos_dados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}

dados_cidade.update(novos_dados)
print(dados_cidade)


# In[14]:


#GET - VERIFICAR SE VARIÁVEL EXISTE.

print(dados_cidade.get('prefeito'))


# In[16]:


print(dados_cidade.keys()) #RETORNA UMA LISTA DE CHAVES DE UM DICIONÁRIO
print('-----')
print(dados_cidade.values()) #RETORNA UMA LISTDA DE VALORES DE UM DICIONÁRIO
print('-----')
print(dados_cidade.items()) #RETORNA UMA LISTA DE TUPLAS (chave, valor) DE UM DICIONÁRIO


# In[ ]:




