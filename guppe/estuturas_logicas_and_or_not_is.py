"""
Estruturas lógicas: and, or, not, is

Operadores unários
    not, is
Operadores binários
    and, or
"""
ativo = True
logado = True
seguro = True
renovado = False

if ativo and logado:
    print('Usuário logado')
else:
    print('Usuário não ativo e logado')

if seguro or renovado:
    print('Tem seguro')
else:
    print('Não tem seguro')

if not ativo:
    print('Não entra aqui')

if ativo is True:
    print('Ativo == True')

