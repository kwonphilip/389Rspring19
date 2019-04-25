#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = open('hashes.txt', 'r')
    pw = open('passwords.txt', 'r')
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    hash_list = []

    for line in hashes:
        hash_list.append(line.rstrip())

    passwords = []

    for p in pw:
        passwords.append(p.rstrip())

    hash_pw = {}

    for c in characters:
        for p in passwords:
            cp = c + p
            cp2 = cp.encode()
            hash_object = hashlib.sha256(cp2).hexdigest()

            hash_pw[hash_object] = cp

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times

    # First hash crack

    data = data.decode('ascii')
    data = data.split()
    data = data[5]

    data2 = hash_pw[data] + '\n'

    #print(data)
    #print(data2)

    time.sleep(1)

    s.send(data2.encode())

    # Second hash crack

    data = s.recv(1024)

    data = data.decode('ascii')
    data = data.split()
    data = data[4]

    data2 = hash_pw[data] + '\n'

    #print(data)
    #print(data2)

    time.sleep(1)

    s.send(data2.encode())

    # Third hash crack

    data = s.recv(1024)

    data = data.decode('ascii')
    data = data.split()
    data = data[3]

    data2 = hash_pw[data] + '\n'

    #print(data)
    #print(data2)

    time.sleep(1)

    s.send(data2.encode())

    # Get the key

    data = s.recv(1024)

    data = data.decode('ascii')

    print(data)


if __name__ == "__main__":
    server_crack()
