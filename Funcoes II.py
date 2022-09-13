#!/usr/bin/env python
# coding: utf-8

# In[1]:


##PARAMETROS VARIAVIES DENTRO DE UMA FUNCAO

def calcular_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[9]:


def calcular_media(*args, margem):#args somente uma conversao do que utilizamos
    soma = sum(args)
    media = soma / len(args)
    return media + margem


# In[10]:


calcular_media(10, 8, 9, margem = 0.3)


# In[13]:


#KWARGS - MAPEADO

def print_info(**kwargs):
    print(kwargs, type(kwargs))


# In[15]:


print_info(nome = "Alexandre", sobrenome = "Barbosa")


# In[ ]:




