# variável
# nome =  'John Connor'

# # separar a string em um lista
# nome_completo = nome.split(' ')

# # exibe a lista
# for parte_nome in nome_completo:
#     print(parte_nome)



# usuário informa o nome 
nome =  input('Informe o seu nome completo:')

# separa as palavras do nome e capitula
nome_lista = nome.split(' ')

# capitular as palavras do nome
for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()
    
# junta o nome em uma variável
nome_completo = ' '.join(nome_lista)

# exibe a lista
print(nome_completo)