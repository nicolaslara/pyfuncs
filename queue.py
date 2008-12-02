"""
This module provides three types of queues, with these constructors:
  Stack([items])  -- Create a Last In First Out queue, implemented as a list
  Queue([items])  -- Create a First In First Out queue
  PriorityQueue([items]) -- Create a queue where minimum item (by <) is first
Here [items] is an optional list of initial items; if omitted, queue is empty.
Each type supports the following methods and functions:
  len(q)          -- number of items in q (also q.__len__())
  q.append(item)  -- add an item to the queue
  q.extend(items) -- add each of the items to the queue
  q.pop()         -- remove and return the "first" item from the queue
"""
import operator

def Stack(items=None):
    "A stack, or last-in-first-out queue, is implemented as a list."
    return items or []

class Queue:
    "A first-in-first-out queue."
    def __init__(self, items=None): self.start = 0; self.A = items or []
    def __len__(self):                return len(self.A) - self.start
    def append(self, item):           self.A.append(item)
    def extend(self, items):          self.A.extend(items)

    def pop(self):
        A = self.A
        item = A[self.start]
        self.start += 1
        if self.start > 100 and self.start > len(A)/2:
            del A[:self.start]
            self.start = 0
        return item

class PriorityQueue:
    "A queue in which the minimum element (as determined by cmp) is first."
    def __init__(self, items=None, cmp=operator.lt):
          self.A = []; self.cmp = cmp;
          if items: self.extend(items)
      
    def __len__(self): return len(self.A)

    def append(self, item):
        A, cmp = self.A, self.cmp
        A.append(item)
        i = len(A) - 1
        while i > 0 and cmp(item, A[i//2]):
            A[i], i = A[i//2], i//2
        A[i] = item

    def extend(self, items):
        for item in items: self.append(item)

    def pop(self):
        A = self.A
        if len(A) == 1: return A.pop()
        e = A[0]
        A[0] = A.pop()
        self.heapify(0)
        return e

    def heapify(self, i):
        "Assumes A is an array whose left and right children are heaps,"
        "move A[i] into the correct position.  See CLR&S p. 130"
        A, cmp = self.A, self.cmp
        left, right, N = 2*i + 1, 2*i + 2, len(A)-1
        if left <= N and cmp(A[left], A[i]):
            smallest = left
        else:
            smallest = i
        if right <= N and cmp(A[right], A[smallest]):
            smallest = right
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.heapify(smallest)
