## Introduction
This is the visualisation of flooding algorithm in computer networking.

## Algorithm of Flooding
Basically in flooding, all nodes act as 
1. Receiver: receives the message sent from the other edge of the link
2. Transmitter: send the message to the other edge of the link

Also, in this network, there are two important events.
1. Deliver event: omit a message
2. Computation event: fulfill a task

So, in flooding, these two events happen in turns.

At first, the root node, which is the first top node in the picture, sends the messages to its children processes. Then children processes will start fulfilling the task accordingly.

## Gifani

## Usage
In case, you don't have it;
`pip install tkinter`


*python3.6 is recommended
`python3 flooding_algo_v2.py`