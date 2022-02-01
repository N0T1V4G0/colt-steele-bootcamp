# ADICIONAR ELEMENTOS - append() extend() insert() 

# append(elemento) adiciona UM elemento ao fim da lista, extend([outros,elementos]) add mais de um elemento.
my_stupid_list = list(range(1,6))
print(my_stupid_list) # [1, 2, 3, 4, 5]
my_stupid_list.extend([6,7])
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7]
my_stupid_list.append(2)
print(my_stupid_list) # # [1, 2, 3, 4, 5, 6, 7, 2]
my_stupid_list.append(['outros', 'elementos'])
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7, 2, ['outros', 'elementos']]
my_stupid_list.pop() # remove último elemento
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7, 2]
# insert(index, elemento) adiciona o elemento ao index passado como argumento.
my_stupid_list.insert(0, 'Oieeee')
print(my_stupid_list) # ['Oieeee', 1, 2, 3, 4, 5, 6, 7, 2]

# REMOVER ELEMENTOS - pop() remove() clear()

# pop(index) remove o elemento no index especificado, retornando o valor.
# Se nenhum argumento for passado, remove e retorna o último elemento.
first_item = my_stupid_list.pop(0)
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7, 2]
print(first_item) # 'Oieeee'
last_item = my_stupid_list.pop()
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7]
print(last_item) # 2
# remove(valueToRemove) remove o elemento do array (apenas a primeira instância)
my_stupid_list.insert(4, 'chegaay')
print(my_stupid_list) # [1, 2, 3, 4, 'chegaay', 5, 6, 7]
my_stupid_list.remove('chegaay')
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7]
# clear() remove todos os elementos do array.
my_stupid_list.clear()
print(my_stupid_list) # []


# Ex removendo elementos que aparecem mais de uma vez na lista.
outra_lista = [1,2,3,4,1,2,3,7,8,2]

for number in outra_lista:
  while number in outra_lista:
    print(number)
    outra_lista.remove(number)

print(outra_lista) # [4, 7, 8]