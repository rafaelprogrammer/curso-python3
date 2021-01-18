"""
Tipo String

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '34', 'True', '43.5'
- Estiver entre àspas duplas -> "uma string", "34", "True", "43.5"
- Estiver entre àspas simples triplas -> '''uma string'''

"""
#- Estiver entre àspas duplas triplas -> """uma string"""

nome = 'Selva selva'
print(nome)
print(type(nome))

nome = "Selva's da Selva's"
print(nome)
print(type(nome))

nome = 'Selva \n da Selva'
print(nome)
print(type(nome))

nome = """Selva
da Selva"""
print(nome)
print(type(nome))

print(nome.upper())
print(nome.lower())
nomeSplit = nome
print(nomeSplit.split()[0])
print(nomeSplit.split())
print(nomeSplit[0:4])
# [::-1] -> Comece do primeiro elemento, vá até o último e inverta
print(nomeSplit[::-1])
print(nome.replace('da', ''))