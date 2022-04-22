"""
Program to perform various function releted to Stacks & Queues.

"""
#---------------------------------STACKS---------------------------------------
def push_stack(stack,item):
    '''
    To push an element into the Stack. 

    Parameters
    ----------
    stack : LIST
        list of umeric characters.
    item : NUMERIC
        Element to be pushed in stack.

    '''
    stack.append(item)
    print(item,"pushed successfully into stack.")

def pop_stack(stack):
    '''
    To pop last element of the stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    if len(stack)==0:
        print("Stack Underflow !!!")
    
    else:
        top=len(stack)-1
        top_element=stack.pop(top)
        print("Element",top_element," poped.")
        

def display_stack(stack):
    '''
    To view stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    length=len(stack)
    if length==0:
        print("Stack is empty.")
        
    else:
        print("Stack is: ")
        for i in range(len(stack)-1, -1, -1):
            print("\t",stack[i])


def peek_stack(stack):
    '''
    To view topmost/last element of the stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    length=len(stack)
    if length==0:
        print("Stack is Empty")
    else:
      print('Topmost element is:',stack[length-1])

#--------------------main--------------------------
stack=[] 
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format("MENU",
            "1. Add element to stack.",
            "2. Remove element from stack.",
            "3. View stack contents.",
            "4. Peek stack.",
            "5. QUIT."
            )

while True:
    print(menu)
    act=input("Enter the serial number of the task you want to perform: ")
    
    if act=='1':
        item=int(input("Enter new element: "))
        push_stack(stack, item)
        
    elif act=='2':
        pop_stack(stack)
        
    elif act=='3':
        display_stack(stack)
        
    elif act=='4':
        peek_stack(stack)
        
    elif act=='5':
        print("Thank you for using this program.")
        break
    
    else:
        print("Please enter valid number !!!")
    
    print("*"*100)


#---------------------------------QUEUES---------------------------------------
def is_empty(queue):
    '''
    To check if Queue is empty or not.
    
    Parameters
    ----------
    queue : LIST
        list of numeric characters.

    Returns
    -------
    bool
        True if empty
        False if not empty.

    '''
    length=len(queue)
    if length==0:
        return True
    else:
        return False
    
def enqueue(queue,element):
    '''
    To add an element to Queue.

    Parameters
    ----------
    queue : LIST
        list of numeric characters.
    element : NUMERIC
        element to be added.

    '''
    global front, rear
    length=len(queue)
    if length==0:
        queue.append(element)
        print(element,"added as First element.")
    else:
        queue.append(element)
        rear+=1
        print(element,"added successfully.")
        
def dequeue(queue):
    '''
    To delete first element of Queue.

    Parameters
    ----------
    queue : LIST
        list of numeric characters.

    '''
    global front, rear
    length=len(queue)
    if length==0:
        print("Queue Underflow.")
    else:
        element=queue.pop(front)
        rear=rear-1
        print(element,"deleted successfully")
        
def display_queue(queue):
    '''
    To display Queue.

    Parameters
    ----------
    queue : LIST
        list of numeric characters.

    '''
    length=len(queue)
    if length==0:
        print("Queue is empty.")
    else:
        print("Queue is :-")
        for i in range(length-1, -1, -1):
            print("\t",queue[i])
            
def peek_queue(queue):
    print("First emlement of the Queue is:",queue[0])

#--------------------main--------------------------
queue=[]
front,rear=0,0
    
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format("MENU",
            "1. Enqueue.",
            "2. Dequeue.",
            "3. View Queue contents.",
            "4. Peek Queue.",
            "5. Check if Queue is Empty.",
            "6. QUIT."
            )

while True:
    print(menu)
    act=input("Enter the serial number of the task you want to perform: ")
    
    if act=='1':
        item=int(input("Enter new element: "))
        enqueue(queue, item)
        
    elif act=='2':
        dequeue(queue)
        
    elif act=='3':
        display_queue(queue)
        
    elif act=='4':
        peek_queue(queue)
        
    elif act=="5":
        if is_empty(queue)==True:
            print("Queue is Empty.")
        else:
            print("Queue in not Empty.")
        
    
    elif act=='6':
        print("Thank you for using this program.")
        break
    
    else:
        print("Please enter valid number !!!")
    
    print("*"*100)
    
#-------------------------------end-of-program---------------------------------