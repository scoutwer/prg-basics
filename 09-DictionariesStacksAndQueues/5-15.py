import queue
import time

q = queue.Queue()

customera = int(input("amount of customers: "))
n = 1
for i in range(customera):
    q.put(n)
    n = n + 1

while q:
    person = q.get()
    print(person)
    time.sleep(3)
    new = input("are there any new persons: ")
    if new == "yes":
        q.put(n)
        n = n + 1
    else: 
        continue
    