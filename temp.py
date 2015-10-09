# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


arquivo = open('/Users/FABIODEV/Documents/arquivo.txt','r')

conteudo = arquivo.readlines()

var = len(conteudo)
valor = []
for i in range(0,var):
    #for j in range(0,7):    
    if(conteudo[i].__contains__('Version')):        
        valor = conteudo[i].split(',')
        for f in valor:
            print f

