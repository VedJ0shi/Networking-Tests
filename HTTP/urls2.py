from urllib.parse import urlencode

#building up a query str from a dict of parameter-value pairs:
query = urlencode({'company': 'Nord/LB', 'report': 'sales', 'name': 'John Doe'})
print(query) 

'''space is replaced by '+' char and '/' is replaced by '%2F' '''

'''Note: a '/' present in the URL is not interpreted by server as a char
but rather as a formal path separation '''


query2 = urlencode({'mode':'topographic', 'pin': 'Boston, MA'})
print(query2)

query3 = urlencode({'mode':'topographic', 'pin': ('Boston, MA', 'Chicago, IL' )}, doseq=True)
print(query3)

