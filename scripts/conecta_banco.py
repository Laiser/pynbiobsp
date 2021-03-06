#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Importa o modulo de conexao com o mysql
import MySQLdb as bd

# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
conn = bd.connect(host="IP DO SERVIDOR", user="USUÁRIO", passwd="SENHA", db="NOME DO BANCO")
# Posiciona o cursor
cursor = conn.cursor()
# Executa a consulta na tabela selecionada
cursor.execute("SELECT * FROM `PESSOAS` WHERE NOME LIKE '%'")
# Conta o numero de linhas na tabela
numrows = int(cursor.rowcount)
# Algumas frescuras
print "--------------------------------------------------"
print "| ID  Campo                                      |"
print "--------------------------------------------------"
# Laço for para retornar os valores, ex.: row[0] primeira coluna, row[1] segunda coluna, row[2] terceira coluna, etc.
for row in cursor.fetchall():
   print " ",row[0]," ",row[1]
# Mais algumas frescuras
print "--------------------------------------------------"
print "|Teste de conexao com o Mysql em python          |"
print "--------------------------------------------------"
