class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_Data = Node(data)
            new_Data.next = self.head
            self.head = new_Data

    
    #printing an element in linkedlist
    def print(self):
        cur_data = self.head

        while cur_data != None:
            print(cur_data.data, end = "-->")
            cur_data = cur_data.next
        print()
    
    def deleteNode(self, data):

        temp = self.head
        
        if temp!= None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        
        while temp!=None:
            if temp.data == data:
                break
            pre = temp
            temp = temp.next

        if temp == None:
            return
        
        pre.next = temp.next

        temp = None    
        
   
    
if __name__ == "__main__":

    ls = LinkedList()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    ls.push(40)
    ls.push(50)

    ls.print()

    ls.deleteNode(40)

    ls.print()



    