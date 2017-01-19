"""Linked List Equality.

A simple Node class, with each node's next data being set as None.

A singly linked list class, without a tail.  It will have a method that 
returns the length of the linked list.  The linked list class will also 
use a Node class, which is also created in this file.

A function to compare two linked lists for their equality, both in length 
and in the data at each node.

"""

class Node(object):
    """Node class."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Singly linked list class, without a tail."""

    def __init__(self, head=None):
        """Initial creation of singly linked list."""
        self._list = []
        self.head = head


    def add_node(self, data):
        """Adds new node to end of list."""

        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)


    def ll_length(self):
        """Returns length of linked list, given the head."""
        
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count



def comp_ll(lst1, lst2):
    """Compares two linked lists to see if they are equal in length and each node's data.

        >>> l1 = LinkedList()
        >>> l1.add_node(3)
        >>> l1.add_node(4)
        >>> l1.add_node(5)
        >>> l2 = LinkedList()
        >>> l2.add_node(3)
        >>> l2.add_node(4)
        >>> l2.add_node(6)
        >>> comp_ll(l1, l2)
        False


        >>> l3 = LinkedList()
        >>> l3.add_node(3)
        >>> l3.add_node(4)
        >>> l3.add_node(5)
        >>> l4 = LinkedList()
        >>> l4.add_node(3)
        >>> l4.add_node(4)
        >>> l4.add_node(5)
        >>> comp_ll(l3, l4)
        True

        >>> l5 = LinkedList()
        >>> l5.add_node(3)
        >>> l5.add_node(4)
        >>> l5.add_node(5)
        >>> l6 = LinkedList()
        >>> l6.add_node(3)
        >>> comp_ll(l5, l6)
        False

    """

    lst1_len = lst1.ll_length()
    lst2_len = lst2.ll_length()

    if lst1_len != lst2_len:
        return False
    else:
        lst1_cur = lst1.head
        lst2_cur = lst2.head

        while lst1_cur:
            if lst1_cur.data != lst2_cur.data:
                return False
            else:
                lst1_cur = lst1_cur.next
                lst2_cur = lst2_cur.next

        return True


#####################################################################
# Docstring tests 

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print



