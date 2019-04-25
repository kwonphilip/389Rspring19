#!/usr/bin/env python3

import hashlib
import string

def crack():
	hashes = open('hashes.txt', 'r')
	pw = open('passwords.txt', 'r')
	characters = string.ascii_lowercase
	
	hash_list = []

	for line in hashes:
		hash_list.append(line.rstrip())

	passwords = []

	for p in pw:
		passwords.append(p.rstrip())

	for c in characters:
		for p in passwords:
			#crack hashes

			# print hashes as 'input:hash'
			# i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

			cp = c + p
			cp2 = cp.encode()
			hash_object = hashlib.sha256(cp2).hexdigest()

			if hash_object in hash_list:
				print(cp + ":" + hash_object)


if __name__ == "__main__":
    crack()
