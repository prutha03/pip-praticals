list=[]
def push(x):
    list.append(x)
def pop():
    if len(list)==0:
        print("stack is empty")
    else:
        print("pop element ",list.pop())

def display():
    print(list)

push(3)
push(4)
push(10)
display()
pop()
pop()
pop()
display()
