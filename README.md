
## Obs: A versão testada foi compilada no gcc versão 5.4.0, na versão 7 ocorreu um erro ainda não solucionado.



## Softwares necessários 

sudo apt-get install raspberrypi-kernel-headers (# somente na RaspBerry)

sudo apt-get install python-pip

pip install --upgrade setuptools

sudo apt-get install python-mysqldb

sudo apt-get install git

pip install pynbiobsp


## Baixar os arquivos:

git clone https://github.com/Laiser/pynbiobsp.git



## Copiar arquivos para a pasta lib(NO PC)

cd pynbiobsp/utils/libs/

sudo cp NBioBSP.lic /lib

sudo cp linux_x86_x64/libNBioBSP.so /lib


## Copiar arquivos para a pasta lib(NO RaspBerry)

cd pynbiobsp/utils/libs/RaspBerry/NBioBSP\ SDK_RaspberryPi\ v1.8940/

sudo cp NBioBSP.lic /lib

sudo cp libNBioBSP.so /lib


## Instalar Driver do leitor biométrico(No PC)

cd ..

cd hamster-iii/

cd ngstardrv-v1.0.5-2-Ubuntu14.04-64bit/

sudo ./CreateModule

sudo ./install.sh


## Instalar Driver do leitor biométrico(Na RaspBerry)

cd ..

cd ngstardrv-v1.0.5-3-patch2-Raspbian-ubuntuMATE-Xubuntu_16.04.2-rpi2_3/

sudo ./install.sh


## Os arquivos para testes estão na pasta /scripts
