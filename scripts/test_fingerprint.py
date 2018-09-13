#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio
import MySQLdb

pnbio.init()

# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
db = MySQLdb.connect(host="200.132.35.233", user="root", passwd="iotclass", db="dbapi")

print('Insert the first fingerprint: ')
fir1 = pnbio.capture(10000)
print fir1;


print('Insert the second fingerprint: ')
fir2 = pnbio.capture(10000)

if pnbio.match(fir1, fir2):
    print('OK!')

# Posiciona o cursor
cursor = db.cursor()
# Executa a consulta na tabela selecionada
sql = "INSERT INTO `BIOMETRIAS`(`ID_BIOMETRIA`, `ID_PESSOA`, `BIOMETRIA`, `IND_MAO`, `DEDO`) VALUES (%s, %s,%s,%s,%s)"
valores = ("1","127","fir1","1","1")
cursor.execute(sql,valores)

#else:
 #   print('NOK!')

pnbio.close()
