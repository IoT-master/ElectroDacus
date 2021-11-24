# ElectroDacus SBMS0 UART Decoder

## This is a WORKING up-to-date Python 3.8 version of decoding Dacian's datalogger

Install the required libraries

>`pip install pyserial`

Use the built-in function using the compressed string from the ElectroDacus

>`python dacian.py`

I highly recommend using virtual environments for a good Python practice

### Disconnect Issues on Raspberry Pi UART Port:
To connect to the device, you need to connect GPIO 14 to the SBMS0's top left pin on the 16 pin connector. You will also need to connect one of the Raspberry Pi's and one of the 3v3 Pin to SBMS0. The 3v3 pin on the SMBS0 is located on either pin on third row COUNT FROM THE BOTTOM on the 16 pin connector. The ground pin of the SMBS0 is located on either pin on the bottom row on the 16 pin connector. See:

>https://pinout.xyz/pinout/uart

Edit the kernel command line with sudo nano /boot/cmdline.txt. Find the console entry that refers to the serial0 device, and remove it, including the baud rate setting. It will look something like console=serial0,115200. Make sure the rest of the line remains the same, as errors in this configuration can stop the Raspberry Pi from booting



# Other Troubleshooting Ideas:
Be sure you enable UART on the SBMS0
sudo vi /boot/cmdline.txt
>console=tty1 root=PARTUUID=3c7b78f1-02 rootfstype=ext4 fsck.repair=yes rootwait
sudo systemctl stop serial-getty@AMA0.service
reboot
enable serial in raspi-config no and then yes
sudo usermod  -a -G tty pi
sudo chmod 666 /dev/ttyAMA0

Open /boot/config.txt file. sudo vi /boot/config.txt
dtoverlay=disable-bt
dtoverlay=pi3-disable-bt

We also need to run to stop BT modem trying to use UART
sudo systemctl disable hciuart

It wasn't easy getting this to work in Python. If you enjoy my work, maybe you can buy me a cup of coffee?

>Bitcoin: 3CrcrfCnr6GNHCJPDc17Z2G8hkkzJo7uGw

>Etherium, Loopring, Shibu Eu: 6b0eee108783fF52Ff2c3477f99C0DE4Df76a4DD

>Monero: 47q8uPAG3Un51nEKshua39U21DQ3VRf5HE3KArLtjyg21Zqs7QPvygx4TXPe2jt7rVGYk6NGizLz3ZRjrQAtGsdhMZCRwLu

>Raptoreum: RJjoD3mrQA9cJ58ghBjpBkRby7m4AgLQRq

>Uniswap: 0xa9b6225c447ef10e27a67c747ce37349be9d8644
