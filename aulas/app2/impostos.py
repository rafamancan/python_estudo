# -*- coding: UTF-8 -*-
# impostos.py
# adicionado no início do arquivo
from abc import ABCMeta, abstractmethod

class Template_de_imposto_condicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if(self.deve_usar_maxima_taxacao(orcamento)):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento): pass

    @abstractmethod
     def maxima_taxacao(self, orcamento): pass

    @abstractmethod
    def minima_taxacao(self, orcamento): pass