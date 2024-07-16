import struct #built-in module for packaging/unpackaging binary data for network communication


#storing numerical strs as bytes using encode():
integer1_str, integer2_str, float_str  = ('6', '111111999990000', '4.734675')
bytes1, bytes2, bytes3 = (integer1_str.encode(), integer2_str.encode(), float_str.encode() )
print(bytes1, bytes2, bytes3)
print(len(bytes1) + len(bytes2) + len(bytes3))
print()
'''bytes1/ bytes2/ bytes3 must be decoded via UTF-8 (or ASCII) and result will be a str
which needs to be further converted back to int or float types'''

#storing ints and floats directly as bytes using pack():
packed_bytes = struct.pack('iif', 6, 199990000, 4.73)
print(packed_bytes) #a single bytes stream
print(len(packed_bytes)) #each number (i or f) takes up 4 bytes
print(struct.unpack('iif', packed_bytes))
print([type(num) for num in struct.unpack('iif', packed_bytes)]) #data types preserved
print()

print(struct.calcsize('i'))
print(struct.calcsize('f')) #both int and float stored in fixed 4 bytes
print(struct.calcsize('iif')) 


'''struct.pack() best for transmission of structured binary information while
.encode() better for transmission of text information i.e. info to be read as a str '''



