#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio
import MySQLdb as bd
from datetime import datetime
from datetime import timedelta

today  = datetime.today()
now_30 = (datetime.now() - timedelta(minutes=30))

# print (str(datetime.now() - timedelta(minutes=30)))
print(now_30.strftime("%H:%M"))
# print(today.weekday() + 1 )
# print(today)
pnbio.init()
	
# string de conexao
conn = bd.connect(host="200.18.32.171", user="root", passwd="#iotcl@ss", db="db_teste")
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


cmd.execute("SELECT ID_PESSOA,BIOMETRIA FROM BIOMETRIA WHERE BIOMETRIA <> ''")

# Conta o numero de linhas na tabela
#numrows = int(cmd.rowcount)

# Algumas frescuras
#print " BUSCANDO BIOMETRIA...."
biometria = cmd.fetchall()
# Laço for para retornar os valores
for row in biometria:
	if pnbio.match(row[1], fir2):
		id_pessoa = row[0]


# GET ID PROFESSOR
cmd.execute("SELECT ID_PROFESSOR FROM PROFESSOR WHERE PESSOA_ID_PESSOA = "+str(id_pessoa))
professor = cmd.fetchone()[0]

# GET ID TURMA PROFESSOR
cmd.execute("SELECT TURMA_ID_TURMA FROM PROFESSOR_TURMA WHERE PROFESSOR_ID_PROFESSOR = "+str(professor))
id_turmas = cmd.fetchall()
turmas = '('
for i, id_turma in enumerate(id_turmas):
	if i > 0:
		turmas += ', '
	turmas += str(id_turma[0])
turmas += ')'


# GET TURMA A PARTIR DO DIA, HORA E PROFESSOR
query = "SELECT * FROM TURMA WHERE ID_TURMA IN "+ turmas +" and ( DIA_SEMANA = "+ str(today.weekday() + 1 ) +" ) and ( HORA_INICIO < '"+ str(now_30.strftime("%H:%M")) +"' and '"+ str(today.strftime("%H:%M")) +"' <= HORA_FIM )"
# print(query)
cmd.execute(query)
turma_do_dia = cmd.fetchall()[0]


# DADOS DA TURMA VIGENTE
id_turma_vigente = turma_do_dia[0]
nome_turma_vigente = turma_do_dia[1]
h_inicio_turma_vigente = turma_do_dia[2]
h_fim_turma_vigente = turma_do_dia[3]


#GET ALUNOS TURMA VIGENTE
query2 = "SELECT MATRICULA, NOME FROM `ALUNO_TURMA` NATURAL JOIN ALUNO NATURAL JOIN PESSOA WHERE ALUNO_TURMA.ID_TURMA =" + str(id_turma_vigente)
print(query2)
cmd.execute(query2)
alunos_turma = cmd.fetchall()
for aluno in alunos_turma:
	print(aluno)










cmd.close()
pnbio.close()