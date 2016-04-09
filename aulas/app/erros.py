# -*- coding: UTF-8 -*-
#erros.py
from models import *
try:
	arquivo = open('perfis.csv', 'r')
	valores = arquivo.readline().split(',')
	Perfil(*valores)
	arquivo.close()
except (IOError, TypeError) as erro:
	print('Deu Error %s' % erro)
finally:
	if(arquivo is not None):
		print('fechando arquivo')
		arquivo.close()