"""
Estrutura de repetição - FOR

"""
nome = 'Selva da Selva'
lista = [1, 2, 3, 4, 5, 6, 7]

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1, 10):
    print(numero)

for index, letra in enumerate(nome):
    print(nome[index])
    print(letra)

# o underline serve para descartar a variavel, no caso, como exemplo, index.
for _, letra in enumerate(nome):
    print(letra, end='')
#https://apps.timwhitlock.info/emoji/tables/unicode

#original: U+1F602
#modificado: U0001F602

for num in range(1, 10):
    print('\U0001F602' * num)