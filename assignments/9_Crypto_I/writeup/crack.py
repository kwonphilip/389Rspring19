#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open('hashes.txt', 'r')
    passwords = open('passwords.txt', 'r')
    characters = string.ascii_lowercase

    hash_list = []

    for line in hashes:
    	hash_list.append(line)

    #for line in hash_list:
    #	print("hash = " + line)

    for c in characters:
        for p in passwords:
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

            cp = c + p.rstrip()
            hash_object = hashlib.sha256(cp.encode()).hexdigest()

            #print("cp = " + cp)
            #print("ho = " + hash_object)
            print("c = " + c)
            print("p = " + p)
            
            for x in hash_list:
            	y = int(x, 16)
            	if y == hash_object:
            		print(cp + ":" + hash_object)


if __name__ == "__main__":
    crack()
