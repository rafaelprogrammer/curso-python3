"""
Listas -> arrays / vetores
Obs: São dinâmicas (Não possui tamanho fixo, e tipos).
Respresentadas por: []
"""
print(type([]))
list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list2 = ['s', 'e', 'e', 'l', 'v', 'a']
print(list2)
list3 = []
print(list3)
list4 = list(range(11))
print(list4)

# contains
num = 8
if num in list4:
    print(f'Contain {num}')
else:
    print(f'Contain {num}')

str = 'e'
if str in list2:
    print(f'Contain {str}')
else:
    print(f'Contain {str}')

# sort
list2.sort()
print(list2)

# count
print(list2.count('e'))
print(list4.count(2))

# adicionar
print(list1)
list1.append(7)
print(list1)

list1.append([8, 5, 6])
print(list1)

if [8, 5, 6] in list1:
    print(f'Encontrou o array [8, 5, 6]')