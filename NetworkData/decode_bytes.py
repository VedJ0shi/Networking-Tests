#bytes object can be converted to a meaningful str object via decode() & an agreed upon encoding

bytes1 = bytes([72,101,108,108,111]) #all these are within printable ASCII range (thus, could also use str declaration)
print(bytes1) #prints bytes object, will be human readable
print(bytes1.decode('utf-8')) #prints str; UTF-8 completely accomodates ASCII 
print()

bytes2 = bytes([240,159,152,138]) #all these ints are outside of printable ASCII range
print(bytes2) #prints bytes object, not human readable (no meaning in ASCII)
print(len(bytes2)) #len of bytes obj is number of bytes
print(bytes2.decode('utf-8')) #decodes via UTF-8 and prints a meaningful str (an emoji)
print(len(bytes2.decode('utf-8'))) #len of str is number of chars


'''while print() privileges the limited 1-to-1 ASCII interpretation of bytes, decode() implements any
interpretation to extract actual meaning from bytes-- UTF-8 is default interpretation/encoding and is variable-to-1'''



