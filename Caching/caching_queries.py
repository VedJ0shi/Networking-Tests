#can cache queries to a stable database
#the key can be the hash of the long str that represents SQL query 
import memcache

mc = memcache.Client(['127.0.0.1:11211']) 

def hash(lookup): #expects SQL str
    ###cryptographic hash function###
    return 

def database_query(lookup):
    ###connects with db service and performs lookup query###
    return

def get_data(lookup): 
    '''can be executed in a loop that reads SQL lookup queries off a file'''
    result = mc.get(hash(lookup))
    if not result:
        result = database_query(lookup) #expensive
        mc.set(hash(lookup), result)
    return result
        

