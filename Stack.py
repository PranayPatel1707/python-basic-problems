#  20CE098, Pranay Patel
#  Practical 8
#  Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal
#  method.

class Stack:
    def __init__(self): 
        self.stck = [] 
    def push(self, data): 
        self.stck.append(data) 
    def pop(self): 
        self.stck.pop()
    def traverse(self): 
        for i in self.stck: 
            print(str(i)+' ')
        print('\n')

s1 = Stack()
run = 1
while(run == 1):
    print('Enter 1 to push')
    print('Enter 2 to pop')
    print('Enter 3 to display')
    print('Enter 4 to exit')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        element = int(input('Enter element to be pushed: '))
        s1.push(element)
        print(element, 'pushed into stack !')
        print()
    elif ch == 2:
        print('Poping topmost element from stack')
        s1.pop()
        print()
    elif ch == 3:
        print('Traversing stack')
        s1.traverse()
    elif ch == 4:
        run = 0
    else:
        print('Enter valid choice')
        print()

