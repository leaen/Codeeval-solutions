import struct

# Find endianness via struct module.

if struct.unpack('<I', struct.pack('=I', 1))[0] == 1:
	print("LittleEndian")
else:
	print("BigEndian")
