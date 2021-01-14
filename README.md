# Consumer-Producer Model

This is a consumer and producer model. Three queues are initiated with random
lengths and are given random values between a certain interval. There is 
one producer and 3 consumers. The producer continuously creates items and 
puts them into the shortest queue available. Each consumer only consumes the 
data in its own queue and when the consumer queues change, it will be 
printed on the console.

## Steps for how to run model on computer:

1.) Install python3 through the terminal
    a.) Python3: https://www.python.org/downloads/

2.) Download or git clone all the source files above

3.) Open producerConsumerReal3.py and run the file either using an IDE or 
    through the terminal using: Python3 producerConsumerReal3.py

4.) The file will write to standard output whenever a producer puts a value
    in the queue or when a consumer reads from its queue

-------------
This model was created by Arnav Arora using Python3