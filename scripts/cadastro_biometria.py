#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio
import MySQLdb

pnbio.init()

#string de conexao
conn = MySQLdb.connect(host="IP DO SERVIDOR", user="USUÁRIO", passwd="SENHA", db="NOME DO BANCO")

print('Posicione o dedo no leitor para realizar a leitura: ')
print('')

# primeira leitura
fir1 = pnbio.capture(10000)
print ('Primeira leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir1);
print('')

# segunda leitura
fir2 = pnbio.capture(10000)
print('Realizando a segunda leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir2);
print('')

# função para verficar leituras
if pnbio.match(fir1, fir2):
    print('Leituras conferidas...')
    print('')

# Posiciona o cursor
cmd = conn.cursor()


try:
   cmd.execute("INSERT INTO BIOMETRIAS(ID_PESSOA, BIOMETRIA, IND_MAO, DEDO) VALUES (%s, %s, %s, %s)",(127,fir1,1,1))
   conn.commit()
   print('Biometria registrada com sucesso!!!')    

except (MySQLdb.Error, MySQLdb.Warning) as e:
   print(e)

 
   
pnbio.close()
