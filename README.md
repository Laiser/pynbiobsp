
## Obs: A versão testada foi compilada no gcc versão 5.4.0, na versão 7 ocorreu um erro ainda não solucionado.



## Instalar 

sudo apt-get install raspberrypi-kernel-headers

sudo apt-get install python-pip

pip install --upgrade setuptools

sudo apt-get install python-mysqldb

sudo apt-get install git

pip install pynbiobsp



## Baixar os arquivos:

git clone https://github.com/Laiser/pynbiobsp.git



## Copiar arquivos para a pasta lib

cd pynbiobsp/utils/libs/

sudo cp NBioBSP.lic /lib

sudo cp linux_x86_x64/libNBioBSP.so /lib


## Instalar Driver do leitor biométrico

cd ..

cd hamster-iii/

cd ngstardrv-v1.0.5-2-Ubuntu14.04-64bit/

sudo ./CreateModule

sudo ./install.sh


## Os arquivos para testes estão na pasta /scripts
