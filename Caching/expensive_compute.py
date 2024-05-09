#measuring performance of a frequently run expensive computation 
#implementing caching with Memcached (not good for Windows)
import memcache, random, time, math

'''Memcached daemon listens on Port 11211'''

mc = memcache.Client(['127.0.0.1:11211']) #different syntax than socket connect call
#pretending our cache stores square roots


def compute(numkey):
    val = mc.get(numkey)
    if val == None: #if not yet cached
        time.sleep(.01)  #pretend sqrt is expensive
        val = math.sqrt(numkey) #do the one-time computation
        mc.set(numkey, val) 
    return val

if __name__ == '__main__':
    trace = []
    for _ in range(1000):
        trace.append(compute(random.randint(0, 20)), time.perf_counter())
    #gradual improvement/convergence of runtime as caching speed-up takes effect
        