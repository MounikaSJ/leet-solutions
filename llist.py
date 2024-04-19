class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


head = Node(1)

nextNode = Node(2)

nextNode.next = Node(3)
head.next = nextNode

count = 0

mainhead = head

while head != None:
    print(head.val)
    head=head.next
    
    count = count+1
print(count)




