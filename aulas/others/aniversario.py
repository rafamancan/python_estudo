# python/aulas/aniversario.py
from datetime import date
print 'Digite o ano em que voce nasceu:'
ano_como_string = raw_input()
ano = int(ano_como_string)
ano_atual = date.today().year
idade = ano_atual - ano
print 'Voce possui ou ira fazer %s anos, no ano de %s.' % (idade,ano_atual)