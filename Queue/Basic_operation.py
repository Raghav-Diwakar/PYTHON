Queue = []
front = None
rear = None

def IsEmpty ():
    if (Queue ==[]):
        return True
    else :
        return False

def EnQueue (q , item ):
    q.append(item)
    if (len(q)==1):
        f=r=0
    else :
        i = len(q) -1 


def DeQueue (q):
    if (IsEmpty(q)):
        return('Underflow')
    else :
        i = q.pop(0)
    if len(q)==0 :
        f = r = None 
    return i 

def Display(q):
    if (len(q)==0 ):
        print("Queue is empty")
    elif(len(q)==1):
        print('front = rear =',q[0])
    else :
        f = 0  
        r =  len(q)-1
        print(q[f],"front",end=" , ")
        for x in range(1,r):
            print(q[x],end=" , ")
        print("rear ",q[r])

while True :
    print("Queue")
    print("1 . enqueue")
    print("2 . dequeue")
    print("3 . display")
    print("4 . exit")
    n  = int(input("enter the choice(1-4)"))
    if n ==1 :
        item = int (input("item to insert"))
        EnQueue(Queue,item)
        # input("press any key ")
    if n == 2 :
        item = DeQueue(Queue)
        if item == 'Underflow':
            print("queue is empty ")
        else :
            print('%d  is dequeue '%item)
        # input("press any key ")

    if n == 3 :
        Display(Queue)
        # input("press any key ")

    if n == 4 :
        break
