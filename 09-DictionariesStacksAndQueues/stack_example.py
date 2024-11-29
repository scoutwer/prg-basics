import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
sum = 0

for i in range(2):
    sum = sum + int(cards.get())

print(sum)


# removes and prints elements from the top of the stack
sum_2 = 0 
while not cards.empty():
    card = cards.get()
    sum_2 = sum_2 + int(card)
    print(card)

print(sum_2)


"""
Note the order of the printed elements.
The last added element is printed first.
"""
