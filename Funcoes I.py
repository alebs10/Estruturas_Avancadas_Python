#!/usr/bin/env python
# coding: utf-8

# In[1]:


#FUNÇÃO É UMA SEQUÊNCIA DE PASSOS NOMEADAS

def hello():
    print("Olá, Mundo!")


# In[2]:


hello()


# In[4]:


def calcular_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[9]:


resultado = calcular_media(9, 10, 8)
print(resultado)


# In[16]:


resultado2 = calcular_media(valor1=9, valor2=10, valor3=9)
print(resultado2)


# In[20]:


print('Olá', end= '')
print(', Ale')


# In[21]:


def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[22]:


resultado = calcula_media()
print(resultado)


# In[ ]:




