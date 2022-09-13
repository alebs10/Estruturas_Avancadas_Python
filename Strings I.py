#!/usr/bin/env python
# coding: utf-8

# In[1]:


empresa = 'Google'
print(empresa, type(empresa))


# In[2]:


empresa = "Amazon"
print(empresa, type(empresa))


# In[3]:


empresa = 'Let's Code


# In[4]:


empresa = "Let's Code"
print(empresa)


# In[6]:


frase = "O professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)


# In[7]:


empresa = 'Google'
print(empresa[0])


# In[9]:


print(empresa[:3])


# In[10]:


nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)


# In[11]:


cabecalho = "             MENU PRINCIPAL            "
print(cabecalho.strip())


# In[12]:


nome_cidade = "rio de janeiro"

print(nome_cidade.title()) #Rio De Janeiro
print(nome_cidade.capitalize()) #Rio de Janeiro
print(nome_cidade.lower()) #rio de janeiro
print(nome_cidade.upper()) #RIO DE JANEIRO


# In[15]:


nome_cidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ")
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != "rio de janeiro":
    print("Tente novamente...")
    nome_cidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ")
    
print("Parabéns campeão!!!")


# In[17]:


mensagem = 'Você viu o que o  Pietro disse na sala ontem ?'
citacao = 'Felipe' in mensagem
print(citacao)


# In[ ]:




