1. Test Environments
  - OS : Raspbian(https://www.raspberrypi.org/downloads/raspbian/)
     * Version:July 2017
     * Release date:2017-07-05
     * Kernel version: 4.9(4.9.35-v7+)
  - OS : ubuntu MATE (https://ubuntu-mate.org/raspberry-pi/)
     * Version: 16.04.2 LTS
     * Kernel version: 4.4.38(4.4.38-v7+)
  - OS : Xubuntu (https://ubuntu-pi-flavour-maker.org/blog/ubuntu-pi-flavours-for-raspberry-pi-3/)
     * Version: 16.04.2
     * Kernel version: 4.4.38(4.4.38-v7+)
   - Device : Raspberry Pi 2/B+(3/B), Nitgen Hamster-II/III

2. Install Driver
  - First, Install Raspberry Pi Kernel-Headers & Build Essential
   $ sudo apt-get install build-essential
   $ sudo apt-get install raspberrypi-kernel-headers
  - Second, Install Hamster-II/III Driver
   . extarct driver package & go to extracted directory
   $ sudo ./install.sh
   ...
   Create Module success.
   NITGEN USB Finkey HAMSTER II/III Driver Install
   'ngstardrv.ko' -> '/lib/modules/4.9.35-v7+/kernel/drivers/usb/misc/ngstardrv.ko'
   'ngstardrv.h' -> '/usr/include/linux/ngstardrv.h'
   './99-Nitgen-ngstardrv.rules' -> '/etc/udev/rules.d/99-Nitgen-ngstardrv.rules'
   NITGEN USB Finkey HAyMSTER II/III Driver sucessfully installed
   Disconnect the Device and Plug it back
   'ngstarlib.so' -> '/lib/ngstarlib.so'
   NITGEN USB Fingkey Hamster II/III Library sucessfully installed

3. UnInstall Driver
   $ sudo ./uninstall.sh
   uninstalling driver.......
   driver un-installed successfully
   uninstalling library.........
   driver un-installed successfully
 
