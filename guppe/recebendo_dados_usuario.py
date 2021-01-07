"""
Recebendo dados do usuário
input() -> todo dado recebido via input é todo tipo string
Em python, string é tudo que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas
"""
# Entrada de dados
#print('Qual é seu nome?')
#nome = input()
nome = input('Qual é seu nome?')

# exemplos de prints
# print('Seja bem-vindo(a) %s' % nome)
# print('Seja bem-vindo(a) {0}'.format(nome))
print(f'Seja bem-vindo(a) {nome}')

# print('Qual é sua idade?')
#idade = input()
idade = input('Qual é sua idade?')

# Processamento

# Saida de dados
print(f'A(O) {nome} tem {idade} anos')

"""
int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro
idade = int(input('Qual é sua idade?'))
"""
print(f'A {nome} nasceu em {2021 - int(idade)}')