######################## INSERTION ############################
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def insertNodeAtHead(llist, data):
    # Write your code here
    newnode = SinglyLinkedListNode(data)
    newnode.next = llist
    llist = newnode
    return llist


def insertNodeAtTail(head, data):
    newnode = SinglyLinkedListNode(data)
    
    if head is None:
        head =  newnode
    else:
        p = head
        while p.next is not None:
            p = p.next
        p.next = newnode   
    return head



def insertNodeAtPosition(head, data, position):
    newnode =  SinglyLinkedListNode(data)

    if head is None:
        head = newnode
    else:
        p = head
        while position > 1:
            p = p.next
            position-=1
        newnode.next = p.next 
        p.next = newnode
    return head 

######################## DELETION ############################

# Delete Linked List Node from a given position
def deleteNode(head, position):
    if position == 0:
        return head.next
    p = head
    for i in range(position-1):
        p = p.next
    p.next = p.next.next
    return head
        
