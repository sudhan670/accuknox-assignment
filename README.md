## accuknox

# Question 1
 By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

 # Answer

Yes it is Synchronously working I implement via the signal demo for running this we need to implement 

# python manage.py test_sync

# Output 

Signal Started
Signal Finished
Question 1: Synchronous Signal
Execution Time: 5.01 seconds

# Question 2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer 

Command to run 

# python manage.py test_thread

# Output

Question 2: Same Thread Check
Caller Thread ID: 13928
Caller Thread ID: 13928

# Question 3

By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# python manage.py test_transaction

# Answer 

How to many times the fresh database caller starts it triggers that many times to run the loop. 

Count: 4 

# Question 4

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

# python rectangle_demo\test_rectangle.py

# Answer 

{'length': 10}
{'breadth': 5}