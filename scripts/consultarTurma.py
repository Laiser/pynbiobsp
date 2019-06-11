#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio
import MySQLdb as bd


pnbio.init()
	
# string de conexao
conn = bd.connect(host="200.18.32.171", user="root", passwd="#iotcl@ss", db="dpapi")
cmd = conn.cursor()

print('Posicione o dedo no leitor para realizar a leitura: ')
print('')

#primeira leitura
fir1 = pnbio.capture(10000)
print ('Primeira leitura:'), ('OK!')
print ('Tamanho do HASH gerado:'), len(fir1)
print ('')

#segunda leitura
fir2 = pnbio.capture(10000)
print('Realizando a segunda leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir2)
print('')

if pnbio.match(fir1, fir2):
	print('As duas leituras conferem!')
	print('')


cmd.execute("SELECT BIOMETRIA FROM BIOMETRIA WHERE BIOMETRIA <> ''")

# Conta o numero de linhas na tabela
#numrows = int(cmd.rowcount)

# Algumas frescuras
#print " BUSCANDO BIOMETRIA...."
resultado = cmd.fetchall()
# Laço for para retornar os valores
for row in resultado:					

	if pnbio.match(row[0], fir2):
		print "--------------------------------------------------"
		print('Biometria ENCONTRADA NO BANCO DE DADOS !')
		print "--------------------------------------------------"
		cmd.close()
		conn.close()
	else:
		print "--------------------------------------------------"
		print('Biometria NÂO ENCONTRADA NO BANCO DE DADOS:(')	
		print "--------------------------------------------------"
		cmd.close()


cmd.close()

pnbio.close()


