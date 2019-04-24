#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open('hashes.txt', 'r')
    passwords = open('passwords.txt', 'r')
    characters = string.ascii_lowercase

    hash_list = []

    for line in hashes:
    	hash_list.append(line.rstrip())

    for c in characters:
        for p in passwords:
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

            cp = c + p.rstrip()
            cp = cp.encode()
            hash_object = hashlib.sha256(cp)

            if hash_object in hash_list:
            	print(p + ":" + hash_object)


if __name__ == "__main__":
    crack()
