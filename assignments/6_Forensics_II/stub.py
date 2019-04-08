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
timestamp = struct.unpack("<L", data[index:index+4])
print("TIMESTAMP: %d" % int(timestamp[0]))
index += 4

author = struct.unpack("<8s", data[index:index+8])
print("AUTHOR: %s" % str(author))
index += 8

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

secCount = struct.unpack("<i", data[index:index+4])
print("SECTION COUNT: %d" % int(secCount[0]))
index += 4

print("-------  BODY  -------")

count = 1
fileLen = len(data)
#fileLen -= index
#print(index)

while index < fileLen:
	print("Section %d" % int(count))
	count += 1

	stype = struct.unpack("<i", data[index:index+4])
	index += 4
	stype = int(stype[0])
	print("stype: %s" % hex(stype))

	slen = struct.unpack("<L", data[index:index+4])
	index += 4
	print("slen: %d" % int(slen[0]))

	if stype == 1:
		svalue = struct.unpack("<%ds" %(slen[0],), data[index:index+slen[0]])
		index += slen[0]
		print("svalue: %s" % str(svalue))
	elif stype == 2:
		svalue = struct.unpack("<%ds" %(slen[0],), data[index:index+slen[0]])
		index += slen[0]
		print("svalue: %s" % str(svalue))
	elif stype == 3:	
		size = int(slen[0]) / 4
				
		for i in range(size):
			svalue = struct.unpack("<i", data[index:index+4])
			index += 4
			print(svalue)

	elif stype == 4:
		size = int(slen[0]) / 8

		for i in range(size):
			svalue = struct.unpack("<d", data[index:index+8])
			index += 8
			print(svalue)

	elif stype == 5:
		size = int(slen[0]) / 8
		
		for i in range(size):
			svalue = struct.unpack("<d", data[index:index+8])
			index += 8
			print(svalue[0])

	elif stype == 6:
		lat, lon = struct.unpack("<dd", data[index:index+16])
		index += 16
		print("Latitute: %f" % float(lat))
		print("Longitude: %f" % float(lon))
	elif stype == 7:
		ref = struct.unpack("<i", data[index:index+4])
		index += 4
		print(ref)
	elif stype == 8:
		buff = data[index:index+slen[0]]
		index += slen[0]
		pngMagic = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
		trailer = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]
		pngMagic += buff
		pngMagic += trailer
		pngMagic = bytearray(pngMagic)
		f = open("Section3.png", "wb")
		f.write(pngMagic)
	elif stype == 9:
		uff = data[index:index+slen[0]]
		index += slen[0]
		pngMagic = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
		trailer = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]
		pngMagic += buff
		pngMagic += trailer
		pngMagic = bytearray(pngMagic)
		f = open("Section4.png", "wb")
		f.write(pngMagic)
	elif stype == 10: 
		uff = data[index:index+slen[0]]
		index += slen[0]
		pngMagic = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
		trailer = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]
		pngMagic += buff
		pngMagic += trailer
		pngMagic = bytearray(pngMagic)
		f = open("Section5.png", "wb")
		f.write(pngMagic)