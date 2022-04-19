

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self):
        self.start_node = None

    def insert_empty(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node

        else:
            print("Empty list")

    # insert element at the end

    def insert_end(self, data):
        # check if list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return

        n = self.start_node

        # iterate till it reaches the end or null

        while n.next is not None:
            n = n.next

        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    # delete the element from the beginning

    def delete_start(self):
        if self.start_node is None:
            print("The LinkedList is empty, nothing to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return

        self.start_node = self.start_node.next
        self.start_prev = None

    # Delete the element from the end

    def delete_end(self):
        # check if list is empty
        
        if self.start_node is None:
            print("The LinkedList is empty, nothing to delete")
            return

        if self.start_node.next is None:
            self.start_node = None
            return

        n = self.start_node
        while n.next is not None:
            n = n.next

        n.prev.next = None

    def display(self):
        if self.start_node is None:
            print("The list is empty")
            return

        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next

        print("\n")



brand_new = DoubleLinkList()

brand_new.insert_empty("tim")
brand_new.insert_end(1)
brand_new.insert_end("Derek")
brand_new.insert_end(2)
brand_new.insert_end("Sam")

# print(brand_new.display())

brand_new.delete_start()

# print(brand_new.display())