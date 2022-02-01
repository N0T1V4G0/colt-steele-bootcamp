# use append() quando for add apenas um elemento à lista, extend() mais de um elemento.
my_stupid_list = list(range(1,6))
my_stupid_list.extend([6,7])
my_stupid_list.append(2)
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7, 2]
# insert(index, elemento) adiciona o elemento ao index passado como argumento.
my_stupid_list.insert(0, 'Oieeee')
print(my_stupid_list) # ['Oieeee', 1, 2, 3, 4, 5, 6, 7, 2]
# pop(index) remove o elemento no index especificado, retornando o valor.
# Se nenhum argumento for passado, remove e retorna o último elemento.
first_item = my_stupid_list.pop(0)
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7, 2]
print(first_item) # 'Oieeee'
last_item = my_stupid_list.pop()
print(my_stupid_list) # [1, 2, 3, 4, 5, 6, 7]
print(last_item) # 2