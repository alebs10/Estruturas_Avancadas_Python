#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CONCATENAÇÃO

comprimento = 'Olá, '
nome = 'Alexandre'
print(comprimento + nome)


# In[2]:


print(nome * 5)


# In[11]:


nome = 'Alexandre'
idade = 20
filhos = 0

#CASTING
idade = str(idade)
filhos = str(filhos)

print(nome + ' tem ' + idade + ' anos'+' e '+ filhos + ' filhos')


# In[12]:


#COM O METODO FORMAT 

print('{} tem {} anos e {} filhos'.format(nome, idade, filhos))


# In[13]:


#FUNÇÃO FORMAT PODE ARREDONDAR VALORES

preco_gasolina = 3.476
print('O preço da gasolina hoje subiu hoje e está em R$: {:.2f}'.format(preco_gasolina))


# In[14]:


f'{nome} tem {idade} anos e {filhos}'


# In[ ]:




