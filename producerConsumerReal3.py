#Arnav Arora
#Consumer and Producer Model

from threading import Thread, Lock, Condition
import time
import random

#generate random lengths for queues
random_int = random.randint(5,10)
random_int2 = random.randint(5,10)
random_int3 = random.randint(5,10)

#queue is a shared variable between producer and consumer
queue1 = [random.randint(1,10) for _ in range(random_int)]
queue2 = [random.randint(1,10) for _ in range(random_int2)]
queue3 = [random.randint(1,10) for _ in range(random_int3)]
# print(len(queue1),len(queue2),len(queue3))
# print((queue1),(queue2),(queue3))

# each queue has its own condition object to notify thread when 
# element is added into the queue
condition_q1 = Condition()
condition_q2 = Condition()
condition_q3 = Condition()

#function finds the shortest queue
#randomly picks one if there are multiple shortest ones
def minLength(a,b,c):
    lenA = len(a)
    lenB = len(b)
    lenC = len(c)
    if(lenA == lenB and lenA == lenC):
        return random.choice([a,b,c])
    elif(lenA < lenB and lenA < lenC):
        return a
    elif(lenB < lenA and lenB < lenC):
        return b
    elif(lenC < lenA and lenC < lenB):
        return c
    elif(lenA == lenB and lenA < lenC):
        return random.choice([a,b])
    elif(lenA < lenB and lenA == lenC):
        return random.choice([a,c])
    elif(lenB == lenA and lenB < lenC):
        return random.choice([a,b])
    elif(lenB < lenA and lenB == lenC):
        return random.choice([b,c])
    elif(lenC == lenA and lenC < lenB):
        return random.choice([a,c])
    else:
        return random.choice([b,c])
    
#produces data and adds to queue
class ProducerThread(Thread):   
    def run(self):
        data = range(5)
        global queue1, queue2, queue3
        while True:
            minQueue = minLength(queue1, queue2, queue3)
            if minQueue == queue1:
                #producer acquires the lock
                condition_q1.acquire()
                num = random.choice(data)
                print("Producer putting in queue 1: ", num)
                # print("Length queue 1: ", len(queue1))
                # print(queue1)
                queue1.append(num)
                # print(queue1)
                #notifies the consumer that there is data in the queue
                condition_q1.notify()
                #releases the lock and now consumer can start consuming
                condition_q1.release()
            elif minQueue == queue2:
                condition_q2.acquire()
                num = random.choice(data)
                print("Producer putting in queue 2: ", num)
                # print("Length queue 2: ", len(queue2))
                # print(queue2)
                queue2.append(num)
                # print(queue2)
                condition_q2.notify()
                condition_q2.release()
            else:
                condition_q3.acquire()
                num = random.choice(data)
                print("Producer putting in queue 3: ", num)
                # print("Length queue 3: ", len(queue3))
                # print(queue3)
                queue3.append(num)
                # print(queue3)
                condition_q3.notify()
                condition_q3.release()
            #sleeping the producer between adding to different queues
            time.sleep(random.random())

#consumes data and removes from the queue
class ConsumerThread(Thread):
    def run(self):
        global queue1
        while True:
            condition_q1.acquire()
            #checks to see if there is data in the queue
            if not queue1:
                #releases lock and blocks consumer from consuming
                condition_q1.wait()
            num = queue1.pop(0)
            print("Consumed from consumer 1: ",num)
            condition_q1.release()
            #allows consumer to check the queue and see if data exists
            #even if the consumer was not notified by the producer
            #random float number between 1 and 2
            time.sleep(random.uniform(1,2))

#consumes data and removes from the queue
class ConsumerThread2(Thread):
    def run(self):
        global queue2
        while True:
            condition_q2.acquire()
            if not queue2:
                condition_q2.wait()
            num = queue2.pop(0)
            print("Consumed from consumer 2: ",num)
            condition_q2.release()
            time.sleep(random.uniform(1,2))

#consumes data and removes from the queue
class ConsumerThread3(Thread):
    def run(self):
        global queue3
        while True:
            condition_q3.acquire()
            if not queue3:
                condition_q3.wait()
            num = queue3.pop(0)
            print("Consumed from consumer 3: ",num)
            condition_q3.release()
            time.sleep(random.uniform(1,2))

ProducerThread().start()
ConsumerThread().start()
ConsumerThread2().start()
ConsumerThread3().start()   