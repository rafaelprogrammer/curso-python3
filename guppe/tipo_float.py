"""
Tipo float

Tipo real, decimal

Casas decimais

Obs: Os separadores de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado no ponto de vista float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuíção
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Converter float para int
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))