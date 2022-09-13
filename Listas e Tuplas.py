#!/usr/bin/env python
# coding: utf-8

# In[1]:


nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(nomes_paises)


# In[2]:


print("Tamanho da Lista: ", len(nomes_paises))


# In[3]:


print('Pais: ', nomes_paises[4])


# In[4]:


print('País: ', nomes_paises[-5])


# In[5]:


print('País: ', nomes_paises[-1])


# In[6]:


nomes_paises[4] = 'Colombia'
print(nomes_paises)


# In[7]:


print('Pais: ', nomes_paises[4])


# In[8]:


print(nomes_paises[1:3])


# In[9]:


print(nomes_paises[1:-1])


# In[10]:


print(nomes_paises[2:])


# In[11]:


print(nomes_paises[:3])


# In[12]:


print(nomes_paises[:])


# In[13]:


print(nomes_paises[::2])


# In[14]:


print(nomes_paises[::-1])


# In[15]:


print('Brasil' in nomes_paises)


# In[16]:


print('Bolonha' in nomes_paises)


# In[17]:


print('Canadá' not in nomes_paises)


# In[18]:


print('Mato Fino do Norte' not in nomes_paises)


# In[19]:


print('Vasco' not in nomes_paises)


# In[20]:


lista_capitais = []


# In[21]:


lista_capitais.append('Brasília')
lista_capitais.append('Tokyo')
lista_capitais.append('Washington')
lista_capitais.append('Paris')
lista_capitais.append('Lisboa')

print(lista_capitais)


# In[22]:


lista_capitais.insert(2, 'Buenos Aires')
print(lista_capitais)


# In[23]:


lista_capitais.remove('Buenos Aires')
print(lista_capitais)


# In[29]:


removido = lista_capitais.pop(3)
print(lista_capitais, removido, type(lista_capitais))


# In[27]:


nomes_paises = 'Argentina', 'Peru', 'EUA', 'Russia', 'Kenya'
print(nomes_paises, type(nomes_paises))


# In[32]:


nome_estado = 'São Paulo',
print(nome_estado, type(nome_estado))


# In[33]:


len(nomes_paises)


# In[35]:


nomes_paises[0]


# In[36]:


a, p, e, r, k = nomes_paises
print(a, e, k)


# In[37]:


print(*nomes_paises)


# In[ ]:




