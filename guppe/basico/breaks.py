"""
Saindo dos loops com break
"""
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)

while True:
    resposta = input('Sair?')
    if resposta == 'sim':
        break
