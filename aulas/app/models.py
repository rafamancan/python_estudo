# -*- coding: utf-8 -*-
class Perfil():
	'Classe para moldar perfis de usuarios'

	def __init__(self, nome, telefone, empresa):
		self.nome 		= nome
		self.telefone 	= telefone
		self.empresa 	= empresa

	def imprimir(self):
		print 'Nome %s, Telfone %s, Empresa %s' % (self.nome, self.telefone, self.empresa)

class Data():
	'Classe para manipular datas'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa():
	'Classe para trabalhar com dados de pessoas'

	def __init__(self, nome, peso, altura):
		self.nome 	= nome
		self.peso 	= peso
		self.altura = altura

	def imprime_imc(self):
		imc = self.peso / (self.altura*self.altura)
		print 'Imc de %s: %s' % (self.nome,imc)

class Perfil(object):
	'Classe padrão para perfis de usuários'
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
	def obter_curtidas(self):
		return self.__curtidas
	def curtir(self):
		self.__curtidas+=1

class Retangulo(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.__area = x * y
	def obter_area(self):
		return self.__area

class Conta(object):
	def __init__(self, titular, saldo):
		self.titular = titular
		self.saldo = saldo
	def calcular_imposto(self): 
		self.saldo = self.saldo * 0.10
		return self.saldo

class ContaCorrente(Conta):
	def __init__(self, titular, saldo):
		super(ContaCorrente, self).__init__(titular, saldo)
	def calcular_imposto(self):
		return super(ContaCorrente, self).calcular_imposto() + 20