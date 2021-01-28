"""
Escopo de variáveis

Dois casos de escopo:

1- variáveis globais;
2- variáveis locais;

Para declarar variáveis em Python
nome_varivel = valor_variavel

Python é um linguagem de tipagem dinâmica.
"""
#variavel global
nome = 'selva'
print(nome)
print(type(nome))

#variavel local
numero = 20

if numero > 10:
    novo = numero + 1
    print(novo)

##aqui so roda se entrar no if
print(novo)