#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynbiobsp as pnbio

pnbio.init()

print('Posicione o dedo no leitor para realizar a leitura: ')
print('')

# primeira leitura
fir1 = pnbio.capture(10000)
print ('Primeira leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir1)
print('')

# segunda leitura
fir2 = pnbio.capture(10000)
print('Realizando a segunda leitura:'), ('OK!')
print('Tamanho do HASH gerado:'), len(fir2)
print('')

if pnbio.match(fir1, fir2):
    print('As duas leituras conferem!')

pnbio.close()
