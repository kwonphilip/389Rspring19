#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

index = 8
offset = 4
timestamp = struct.unpack("<L", data[index:index+offset])
print("TIMESTAMP: %d" % int(timestamp[0]))

index += offset
offset = 8
author = struct.unpack("<8s", data[index:index+offset])
print("AUTHOR: %s" % str(author))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

count = 1
print("Section %d" % int(count))
count += 1

index += offset
offset = 4
stype = struct.unpack("<L", data[index:index+offset])
stype = int(stype[0])
print("stype: %s" % hex(stype))

index += offset
slen = struct.unpack("<L", data[index:index+offset])
print("slen: %d" % int(slen[0]))

if stype == 1:
	index += offset
	offset = 8*slen
	svalue = struct.unpack("<8s", data[index:index+offset])
	print("svalue: %s" % str(svalue))
elif stype == 2:
	index += offset
	offset = 8*slen
	svalue = struct.unpack("<8s", data[index:index+offset])
	print("svalue: %s" % str(svalue))

elif stype == 3:	
	size = int(slen[0]) / 4
			
	for i in range(size):
		index += offset
		offset = 4
		svalue = struct.unpack("<L", data[index:index+offset])
		print(svalue)

elif stype == 4:
	size = int(slen[0]) / 8

	for i in range(size):
		index += offset
		offset = 8
		svalue = struct.unpack("<LL", data[index:index+offset])
		print(svalue)

elif stype == 5:
	#size = int(slen[0]) / 8
	size = int(slen[0])
	for i in range(size):
		index += offset
		offset = 8
		svalue = struct.unpack("<d", data[index:index+offset])
		print(svalue[0])

#elif stype == 6:
#elif stype == 7:
#elif stype == 8:
#elif stype == 9:
#elif stype == 10: