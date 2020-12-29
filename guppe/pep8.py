"""
PEP 8 -- Python Enhancement Proposals

São propostas de melhorias para a linguagem python

The Zen  of Python

import this

A ideia do PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nome de classes.
class Calculadora:
    pass
class CalculdadoraCientifica:
    pass

[2] - Utilize nomes em mínusculos, separados por underline para funções ou variáveis.
def soma():
    pass
numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação
if 'a' in 'banana':
    print('existe')

[4] - Linhas em branco
- separar funções e definições de classes com duas linhas em branco.
- métodos dentro de uma classe devem ser separados com uma única linha em branco.

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas:
# Import errado
import sys, os

# Import certo
import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import {
  StringType,
  ListType,
  SetType,
  OutroType
}

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docsstring e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões de instruções.

"""





