"""
Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become
5->12->7->10->17->2->13->4->11->6 and second list should become empty.

The nodes of second list should only be inserted when there are positions available.
For example, if the first list is 1->2->3 and second list is 4->5->6->7->8,
then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e.,
 insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.
"""

class LinkedList:
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def merge(self,q):
        p_curr = self.head
        q_curr = q.head

        while p_curr != None and q_curr != None:
            p_next = p_curr.next
            q_next = q_curr.next

            q_curr.next = p_next
            p_curr.next = q_curr

            p_curr = p_next
            q_curr = q_next

        q.head = q_curr

    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        print(' ')

# Driver program to test above functions
llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(3)
llist1.push(2)
llist1.push(1)

print("First Linked List:")
llist1.printList()

llist2.push(8)
llist2.push(7)
llist2.push(6)
llist2.push(5)
llist2.push(4)

print("Second Linked List:")

llist2.printList()
llist1.merge(llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()