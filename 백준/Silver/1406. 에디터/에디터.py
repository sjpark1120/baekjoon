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


n = input() #문자열
n_list = LinkedList()
for i in range(len(n)):
    n_list.add_node(n_list.tail, n[i])
m = int(input())

for i in range(m):
    commad = list(sys.stdin.readline().split())
    if commad[0] == 'L':
        if n_list.cur.prev.prev != None:
            n_list.cur = n_list.cur.prev
    elif commad[0] == 'D':
        if n_list.cur.next != None:
            n_list.cur = n_list.cur.next
    elif commad[0] == 'B':
        if n_list.cur.prev.prev != None:
            n_list.delete_node(n_list.cur.prev)
    elif commad[0] == 'P':
        word = commad[1]
        n_list.add_node(n_list.cur, word)
n_list.print_all()