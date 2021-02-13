#!/home/kali python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet kaba kuvvet")
print("""
kaba kuvvet aracina hos geldin

1) FTP
2) SSH
3) telnet
4) http
5) smb
6) rop
7) sip
8) redis
9) vnc
10) postgresql
11) mysql

""")
islemno = raw_input("islem numarasini girin: ")
hedefip = raw_input("hedef ip girin: ")
kullaniciadi = raw_input("kullanici adi dosya yolu: ")
sifre = raw_input("wordlist yolu: ")
 
if(islemno=="1"):
      os.system("ncrack -p 21 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
elif(islemno=="2"):
      os.system("ncrack -p 22 " + kullaniciadi + " -P " + sifre + " " + hedefip)
      
