#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio
import MySQLdb

pnbio.init()

# string de conexao
conn = MySQLdb.connect(host="200.132.35.233", user="root", passwd="iotclass", db="dbapi")
cmd = conn.cursor()

print('Posicione o dedo no leitor para realizar a leitura: ')
print('')

#primeira leitura
fir1 = pnbio.capture(10000)
print ('Primeira leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir1);
print('')

#segunda leitura
fir2 = pnbio.capture(10000)
print('Realizando a segunda leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir2);
print('')

if pnbio.match(fir1, fir2):
    print('As duas leituras conferem!')
    print('')


cmd.execute("SELECT BIOMETRIA FROM BIOMETRIAS WHERE BIOMETRIA <> '' ")

# Conta o numero de linhas na tabela
numrows = int(cmd.rowcount)

# Algumas frescuras

print " BUSCANDO BIOMETRIA...."

# Laço for para retornar os valores, ex.: row[0] primeira coluna, row[1] segunda coluna, row[2] terceira coluna, etc.
for row in cmd.fetchall():

	if pnbio.match(row[0], fir2):
		print "--------------------------------------------------"
		print('Biometria ENCONTRADA NO BANCO DE DADOS !')
		print "--------------------------------------------------"
	else:
		print "--------------------------------------------------"
		print('Biometria NÂO ENCONTRADA NO BANCO DE DADOS:(')	
		print "--------------------------------------------------"

pnbio.close()
