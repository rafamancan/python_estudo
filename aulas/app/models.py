# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    # para testar via terminal
    # >>> from models import Perfil
    # >>> perfis = Perfil.gerar_perfis('perfis.csv')
    # >>> for p in perfis:
    # ...         p.imprimir()
    @staticmethod
    def gerar_perfis(nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            # caso atenda a condicao, o codigo abaixo sera omitido
            if(len(valores) is not 3):
            	raise ArgumentoInvalidoErro('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
            perfis.append(Perfil(*valores))
        arquivo.close()
        return perfis

class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários VIPs'

    def __init__(self, nome, telefone, empresa, apelido):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

class ArgumentoInvalidoErro(Exception):
	def __init__(self, mensagem):
		self.mensagem  = mensagem
	def __str__(self):
		return repr(self.mensagem)