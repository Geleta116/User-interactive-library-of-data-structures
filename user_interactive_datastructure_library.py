






#THE BELOW CODE IS THE IMPLEMENTATION OF THE CODE TO CREATE A NODE
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None
        
#THE BELOW CODE IS THE IMPLEMENTATION OF THE SINGLY LINKED LIST        
class Singly_Linked_list:

        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
        def addFirst(self, element):
            newNode = Node(element)
            if self.size == 0:
                self.head = newNode
                self.tail = newNode

            else:
                newNode.next = self.head
                self.head = newNode
            self.size += 1
            
        def addLast(self, element):
            newNode = Node(element)
            if self.size == 0:
                self.head = newNode
                self.tail = newNode
                self.size += 1
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.size += 1
        def insert(self, index, element):
            newNode = Node(element)
            currentIndex = 0
            if index == 0:
                self.addFirst(element)

            elif self.size < index:
                self.addLast(element)

            else:
                currentNode = self.head
                while index - 1 != currentIndex:
                    currentNode = currentNode.next
                    currentIndex += 1

                thirdNode = currentNode.next
                currentNode.next = newNode
                newNode.next = thirdNode
                self.size += 1
        def removeFirst(self):
            if self.head is None:
                print("Empty Linked List")

            nodeToRemove = self.head
            newhead = self.head.next
            self.head = newhead
            nodeToRemove = None
            self.size -= 1
        def removeLast(self):#err
            currentNode = self.head
            newtail = self.head
            if self.size == 0:
                print("Empty Linked List")
            else:
                while currentNode.next is not None:
                    newtail = currentNode
                    currentNode = currentNode.next

                self.tail = newtail
                newtail.next = None
                self.size -= 1
             
            
            
        def removeAt(self, index):
            if index == 0:
                self.removeFirst()

            elif index > self.size or index < 0:
                print("Index out of bound")
                return

            else:
                temp = self.head
                for i in range(1, index-1):
                    temp = temp.next
                nodeToDelete = temp.next
                temp.next = temp.next.next
                nodeToDelete = None
                self.size -=1
            

        def isEmpty(self):
            print(self.size== 0)
            

        def getSize(self):
             print("the size of the linked list is " + str(self.size))


        def __str__(self):
          current = self.head
          result = "["
          for i in range(self.size):
            result += str(current.element)
            current = current.next

            if current != None:
                result += ", "
            else:
                result += "]"
                print( result)
                return
     
#THE BELOW CODE IS THE IMPLEMENTATION OF THE STACK DATA STRUCTURE        
class Stack:
    
    def __init__(self):
        self.newstack = []

    def isEmpty(self):
        if (len(self.newstack) == 0):
            print( True)
        else:
            print( False)
        return(len(self.newstack) == 0)


    def push(self,item):
        self.newstack.append(item)
        print("pushed item: " + str(item))

    def pop(self):
        if (len(self.newstack) == 0):
            print("stack is empty")

        else:
            print(self.newstack.pop())


    def peek(self):
        if (len(self.newstack) == 0):
            print(None)
        else:
            print(self.newstack[len(self.newstack) - 1])
    def print_current_stack(self):
        print(self.newstack)
            

        

#THE BELOW CODE IS THE IMPLEMENTATION OF THE CIRCULAR LINKED LIST 

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def addToEmpty(self, element):
        newNode = Node(element)
        self.head = self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
    def addFirst(self,element):
        newNode = Node(element)
        if self.size == 0:
            self.head = self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        self.size +=1

    def addLast(self,element):
        newNode = Node(element)
        if self.size == 0:
            self.head = self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail = newNode
        self.size +=1


    def addAt(self,element,index):
        newNode = Node(element)
        if index == 0:
            self.addFirst(element)
        elif index > self.size-1:
            self.addLast(element)

        else:
            currentNode = self.head
            ind = 0
            while ind< (index - 1):
                currentNode = currentNode.next
                ind += 1

            temp = currentNode.next
            currentNode.next = newNode
            newNode.next = temp
            temp.prev = newNode
            newNode.prev = currentNode
        self.size += 1

    def removefirst(self):
        if self.size == 0:
            print("you cant remove from an empty circular doubly linked list")
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1

        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.size -=1



    def removeLast(self):
        if self.size == 0:
            print("you cant remove from an empty circular doubly linked list")
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.tail.next = self.head
            self.head.prev = None
            self.head.prev = self.tail
            self.size-=1
    def removeAt(self,index):
        if self.size == 0:
            print("you can't remove from an empty circular linked list")
        elif self.size ==1:
            self.head = self.tail = None
            self.size-=1
        elif index == 0:
            self.removefirst()


        elif index>=1 and index<self.size-1:
            ind = 0
            currentNode = self.head
            while ind < (index):
                currentNode = currentNode.next
                ind += 1
            temp = currentNode.next
            currentNode.prev.next = temp
            temp.prev = currentNode.prev
            currentNode = None
            self.size -=1
        elif index>=self.size-1:
            print("Index out of range")

    def print_circular_linked_list(self):
        if self.tail == None:
            print("The list is empty")
            return

        newNode = self.tail.next
        while newNode:
            print(newNode.element, end=" ")
            newNode = newNode.next
            if newNode == self.tail.next:
                break
        print("\n")

#THE BELOW CODE IS THE IMPLEMENTATION OF THE QUEUE DATA STRUCTURE USING THE SINGLY LINKED LIST 
class Queue:
    def __init__(self):
        self.list = Singly_Linked_list()

    def enqueue(self, element):
        self.list.addLast(element)

    def dequeue(self):
        if self.list.size == 0:
            return None
        else:
            return self.list.removeFirst()
    def getSize(self):
        return self.list.getSize()
    def __str__(self):
        return self.list.__str__()




        
#The below code is the implementation of DOUBLY LINKED LIST
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, index, new_data):
        size=self.getSize()
        if index<0:
            return
        if index>size:
            self.append(new_data)
            return
        current=self.head
        if current is None:
            return

        counter=index
        while counter>0 and current!=None:
            current=current.next
            counter-=1
        prev_node=current
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def printList(self,choice):
        Doubleforward=[]
        Doublebackward=[]
        node=self.head
        curr=node
        last=self.head
        while curr:
            last=curr
            curr=curr.next
        if choice==1:
            while node:
                Doubleforward.append(node.element)
                node = node.next
            print(Doubleforward)
        else:
            while last:
                Doublebackward.append(last.element)
                last = last.prev
            print(Doublebackward)
    def getSize(self):
        curr=self.head
        size=0
        if not curr:
            return 0
        while curr.next:
            curr=curr.next
            size+=1
        return size
















#THE BELOW CODE  IS A USER INTERACTIVE METHOD THAT COMMUNICATES WITH A USER
#IT CREATES A DATASTRUCTURE BASED ON THE DESIRES OF A USER AND PERFORMES ACTION ON THEM
'''
                                process OF USING CODE
The code first prompts the user to enter the form o data structure they want to create and manipulates
and then using the code that we have provided for it the code creates the data structure that the user wants
then the code prompts the user to enter a number for specific actions that can be taken on
the data structure created.
The only thing expected from the user to create and manipulate such data types is to follow the insructions
that we have provided for them

'''
            
    
def main():
    Data_structure_Number = int(input('''please enter the following numbers that you want to access
1. Singly Linked list
2. Stack
3. Queue
4. circular linked list
5. doubly linked list
choose an action:  '''))


    
    if  Data_structure_Number == 1:
        singly_Linked_list = Singly_Linked_list()
        choosen_action = 0
        while choosen_action != 10:
                choosen_action = int(input('''please enter the respective numbers depending on the action you want to take on the singly linked list
1.Add an element to the linked list
2.Add an element to the end of the linked lsit
3. Add an element at the given index in the linked list
4. Remove the first element from the linked list
5. Remove the last element from the linked list
6. Remove at a given index
7. Check if the linked list is empty
8. get the size of the linked list
9. print out the singly linked list
10. To finish the action taken on the singly linked list and display the created linked list
choose an action: '''))
                if choosen_action == 1:
                    element = int(input("please enter the element to be added at the first of the linked list :  "))
                    singly_Linked_list.addFirst(element)
                    singly_Linked_list.__str__()
                elif choosen_action == 2:
                    element = int(input("please enter the element to be added at the end of the linked list : "))
                    singly_Linked_list.addLast(element)
                    singly_Linked_list.__str__()
                elif choosen_action == 3:
                    index  = int(input("Enter the index at which you want to add the element : "))
                    element =  int(input("please enter the element to be added at the end of the linked list : "))
                    singly_Linked_list.insert(index, element)
                    singly_Linked_list.__str__()
                elif choosen_action == 4:
                    singly_Linked_list.removeFirst()
                    singly_Linked_list.__str__()
                elif choosen_action == 5:
                    singly_Linked_list.removeLast()
                    singly_Linked_list.__str__()
                elif choosen_action == 6:
                    index  = int(input("Enter the index at which you want to remove an element: "))
                    singly_Linked_list.removeAt(index)
                    singly_Linked_list.__str__()
                elif choosen_action == 7:
                    singly_Linked_list.isEmpty()
                elif choosen_action == 8 :
                    singly_Linked_list.getSize()
                elif choosen_action == 9:
                    singly_Linked_list.__str__()
                elif choosen_action == 10:
                     print("number of alterations completed")
                     break
                else:
                    print("That is not a valid input")
       
        print("you have created the singly linked list below")
        singly_Linked_list.__str__()
            
            
            
        
                        
    elif  Data_structure_Number == 2:
        stack = Stack()
        choosen_action = 0
        while choosen_action != 6:
            choosen_action = int(input('''please enter the corresponding numbers for the alterations you want to make to your stack
1. push an element to the stack
2. pop an element from the stack
3. check if the stack is Empty
4. peek the top most element of the stack
5.print the current stack
6. to terminate editing the stack
choose an action: '''))
            if choosen_action == 1:
                element = int(input("please enter the element to be pushed to the stack : "))
                stack.push(element)
            elif choosen_action ==  2:
                stack.pop()
            elif choosen_action == 3:
                stack.isEmpty()
            elif choosen_action == 4:
                stack.peek()
            elif choosen_action == 5:
                stack.print_current_stack()
            elif choosen_action == 6:
                print("Number of alterations on your stack is completed")
                break  
            else:
                print("That is not a valid input")
        
        print("You created the below stack")
        print(stack.newstack)
      

        
    elif  Data_structure_Number == 3:
        queue = Queue()
        choosen_action = 0
        while choosen_action != 5:
            choosen_action = int(input('''enter the number corresponding to the action you want to take on the Queue
1. Enqueue an element
2. Dequeue a queue
3. get the size of the queue
4. print out the queue
5. Terminate the action on the queue
choose an action: '''))
            if choosen_action == 1:
                element = int(input("Enter the element to be Enqueued to the Queue: "))
                queue.enqueue(element)
            elif choosen_action == 2:
                queue.dequeue()
            elif choosen_action == 3:
                queue.getSize()
            elif choosen_action == 4:
                queue.__str__()
            elif choosen_action == 5:
                break
            else:
                print("That is not a valid input")
        print("Number of alteratioms on your Queue is completed")
        print(queue.__str__())







                
            
    elif  Data_structure_Number == 4:
        circular_linked_list = CircularLinkedList()
        choosen_action = 0
        while choosen_action != 8:
            choosen_action = int(input(''' please enter the following number depending on what you want to do to your circular linked list
1. Add to an Empty circular linked list
2. Add to the Front of a circular linked list
3. Add to the end of your circular linked list
4. Remove the first element from the linked list
5. Remove the last element from the linked list
6. Remove the element at a given Node
7. traverse and print the elements in the circular linked list
8. Terminate the action taken on the circular linked list 
choose an acton: '''))
            if choosen_action == 1:
                element = int(input("please enter the element that you want to be added to the empty circular linked list: "))
                circular_linked_list.addToEmpty(element)
            elif choosen_action == 2:
                element = int(input("please enter the element that you want to be added to the front of the circular linked list: "))
                circular_linked_list.addFirst(element)
            elif choosen_action == 3:
                element = int(input("please enter the element that you want to be added to the front of the circular linked list: "))
                circular_linked_list.addLast(element)
            elif choosen_action == 4:
                circular_linked_list.removefirst()
            elif choosen_action == 5:
                circular_linked_list.removeLast()
            elif choosen_action == 6:
                index = int(input("please enter the index of the element which you want to remove: "))
                circular_linked_list.removeAt(index)
            elif choosen_action == 7:
                circular_linked_list.print_circular_linked_list()
            elif choosen_action == 8:
                circular_linked_list.print_circular_linked_list()
                break
                  
            else:
                print("That is not a valid input")
                break


                
                    
    elif Data_structure_Number == 5:
            doubly_linked_list = DoublyLinkedList()

            while True:
                choosen_action = int(input(''' please enter the corresponding numbers depending on the actions you want to take on the doubly linked list
    1. Adding an element to the front of the doubly linked list
    2. Inserting a node after a given previous node
    3. Appending an element to a doubly linked list
    4. printing out the doubly linked list created
    5. To terminate the actions taken on the doubly linked list
    choose an actoin: '''))
                if choosen_action == 1:
                    element = int(input(" please enter the element you wish to push to the linked list : "))
                    doubly_linked_list.addFirst(element)
                elif choosen_action == 2:
                    index=int(input("enter the index: "))
                    element = int(input(" please enter the element you wish to Inserting after a node : "))
                    doubly_linked_list.insertAfter(index,element)

                elif choosen_action == 3:
                    element = int(input(" please enter the element you wish to append to the linked list : "))
                    doubly_linked_list.append(element)

                elif choosen_action == 4:
                    choice=int(input("enter your choice\n1. to traverse in forward direction \n 2. to traverse in backward direction\n"))
                    doubly_linked_list.printList(choice)
                elif choosen_action == 5:
                    break

                else:
                    print("That is not a valid input")
                    break
            
            
            
            
        
            
main()


