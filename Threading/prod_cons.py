import threading, random
import concurrent.futures as cfutures

'''general design: there is a Producer thread that reads from the 
fake network and puts messages into a Pipeline; the Consumer thread can
pull messages from the Pipeline to write to a database that is rate-limited'''

class Pipeline:
    """Class to allow a *single element* pipeline between producer and consumer."""

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() #state to start in; consumer must first wait until producer updates message in pipeline

    def get_message(self):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release() #allows producer to update value of message attribute
        return message

    def set_message(self, message): 
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release() #allows consumer to read value of message attribute


def producer(pipeline):
    """Pretend we're getting a message from the network and putting it in the pipeline"""
    for i in range(10):
        message = random.randint(1, 101) #fake message
        print("Producer got message from network:", message)
        pipeline.set_message(message)

    pipeline.set_message('EoF')

def consumer(pipeline):
    """Pretend we're accessing database and storing message from pipeline into it"""
    message = 0
    while message != 'EoF':
        message = pipeline.get_message()
        print("Consumer storing message in database:", message)


if __name__ == "__main__":
    '''scheduling two threads (with targets consumer & producer) interacting with shared Pipeline object'''
    mypipeline = Pipeline()
    with cfutures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, mypipeline)
        executor.submit(consumer, mypipeline)