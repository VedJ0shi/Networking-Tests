#bytes objects have no intrinsic meaning, even if they are printed and display ASCII chars
#Python tries to print bytes objects in a maximally human readable format by mapping byte values to ASCII
#meaning of bytes depends entirely on encoding i.e. ASCII encoding is default for prints

'''Two ways to declare a bytes object: 1.str declaration or 2.byte-by-byte declaration'''
'''syntax for a bytes object is b'<>', which is similar to str objects ('<>')'''

'''1. directly declared by an ASCII str inside <>, where the Printable ASCII chars
 like English letters, digits and punctuation correspond to byte values in range(32,127)
'''
'''2.bytes() function can convert list of ints (each represents one byte) into a bytes object-- 
thus, max int value is 255 and ints in range(32, 127) will be human-readable when printed'''

byte_range = [n for n in range(0,256)] #list of raw ints accessed for byte-by-byte declarations

print(bytes(byte_range))
print(bytes(byte_range[32:127])) #printable ASCII chars
print(bytes(byte_range[48:58])) #digits
print(bytes([72,101,108,108,111,32,33])) 
print(b'Hello !' == bytes([72,101,108,108,111,32,33])) #str declaration equivalent to byte-by-byte

try:
    print(bytes([256, 257, 258]))
except:
    print('given integer out of range for one byte')


'''byte-by-byte declaraion is more general since it accomodates byte values outside
the printable ASCII ones (outside of range(32,127))'''

#https://stackoverflow.com/questions/14690159/is-ascii-code-in-matter-of-fact-7-bit-or-8-bit
    
