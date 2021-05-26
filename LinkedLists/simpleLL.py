class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head=node
    
    def insert_at_position(self,data,position):
        if self.head is None:
            self.head=Node(data,self.head)
            return
        node=Node(data,None)
        itr=self.head
        for i in range(position-1):
            itr=itr.next
        node.next=itr.next
        itr.next=node

    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        node=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node

    def delete_last(self):
        if self.head is None:
            print("List is Empty")
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

    def delete_at_position(self,position):
        if self.head is None:
            print("List is Empty")
            return
        if position == 0:
            self.head=self.head.next
            return
        
        itr=self.head
        for i in range(position-1):
            itr=itr.next
        itr.next=itr.next.next
    

    def printLL(self):
        if self.head is None:
            print("Linked is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '-->'
            itr=itr.next
        print(llstr)
    


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(2)
    ll.printLL()
    ll.insert_at_position(3,1)
    ll.insert_at_position(4,2)
    ll.insert_at_position(10,3)
    ll.printLL()
    ll.insert_at_last(7)
    ll.printLL()
    ll.delete_last()
    ll.printLL()
    ll.delete_at_position(3)
    ll.printLL()