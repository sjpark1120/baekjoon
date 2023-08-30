import sys
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next#다음 노드의 주소
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.cur = self.tail
    
    def print_all(self):
        curp = self.head.next
        while curp != self.tail:
            print(curp.data, end='')
            curp = curp.next
    
    def add_node(self, p, value):
        prev_node = p.prev
        new_node = Node(value, prev_node, p)
        p.prev = new_node
        prev_node.next = new_node

    def delete_node(self, x):
        prev_node = x.prev
        next_node = x.next
        prev_node.next = next_node
        next_node.prev = prev_node

n = int(input())

for i in range(n):
    password = list(input())
    n_list = LinkedList()

    for j in password:
        if j == '<':
            if n_list.cur.prev.prev != None:
                n_list.cur = n_list.cur.prev
        elif j == '>':
            if n_list.cur.next != None:
                n_list.cur = n_list.cur.next
        elif j == '-':
            if n_list.cur.prev.prev != None:
                n_list.delete_node(n_list.cur.prev)
        else:
            word = j
            n_list.add_node(n_list.cur, word)
    n_list.print_all()
    print()