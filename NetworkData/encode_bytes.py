#str declaration of bytes object (b'<>') assumes ASCII encoding; encode() is more general

'''ASCII character encoded to exactly one byte in UTF-8 (1-to-1)'''
str1 = 'Hello'
print(b'Hello')
print(str1.encode('utf-8'))
print(len(str1), len(str1.encode('utf-8'))) #match since UTF-8 includes ASCII (1-to-1)
print(str1[0], b'Hello'[0]) #latter will be the first byte value (ASCII value of H)
bytes1 = []
for byte in b'Hello':
    bytes1.append(byte) #byte is a raw byte value based on ASCII mappings of H,e,l,o
print(bytes1) 
print()

str2 = '12345000'
print(b'12345000')
print(str2.encode('utf-8'))
print(len(str2), len(str2.encode('utf-8'))) #match
print(str2[0], b'12345000'[0]) #latter will be the first byte value (ASCII value of 1)
bytes2 = []
for byte in b'12345000':
    bytes2.append(byte)
print(bytes2)
print()

'''special character may be encoded to multiple bytes in UTF-8 (var-to-1)'''
str3 = 'Hällo'
print(str3.encode('utf-8'))
print(len(str3), len(str3.encode('utf-8'))) #will not match; ä maps to 2 bytes in UTF-8
print(str3[0], str3.encode('utf-8')[0]) #latter will be the first byte value (ASCII value of H)
bytes3 = []
for byte in str3.encode('utf-8'):
    bytes3.append(byte)
print(bytes3) #2nd and 3rd byte values will be interpreted as a composite code number









