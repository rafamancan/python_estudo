# python/aulas/app.py
# -*- coding: UTF-8 -*-
import re
def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual nome voce gostaria de remover?'
	nome = raw_input()
	nomes.remove(nome)


def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_remover = raw_input()
    if(nome_a_remover in nomes):
        posicao = nomes.index(nome_a_remover)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo
    else:
    	print 'Este nome nao constra na lista!'

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome = raw_input()
    if(nome in nomes):
        print "Nome %s está cadastrado" % (nome)
    else:
        print "Nome %s não está cadastrado" % (nome)

def terminar():
	print 'Vejo voce mais tarde... ;)'
	
def procurar_regex(nomes):
	print 'Digite a expressao regular'
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	resultado = re.findall(regex,nomes_concatenados)
	print resultado

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite: 1 para cadastrar, 2 para listar, 3 para excluir, 4 para alterar, 5 para procurar, 6 expressao regular e 0 para terminar.'
		escolha = raw_input()

		if(escolha == '1'):
			cadastrar(nomes)
		elif(escolha == '2'):
			listar(nomes)
		elif(escolha == '3'):
			remover(nomes)
		elif(escolha == '4'):
			alterar(nomes)
		elif(escolha == '5'):
			procurar(nomes)
		elif(escolha == '6'):
			procurar_regex(nomes)
		elif(escolha == '0'):
			terminar()
		else:
			print 'Opcao invalida, tente novamente!'

menu()