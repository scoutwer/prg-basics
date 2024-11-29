import queue

binary = queue.LifoQueue()
number = int(input("Number: "))

while number != 0:
    if number % 2 == 0:
        binary.put(0)
    elif number %2 == 1:
        binary.put(1)
    number = number // 2 

while not binary.empty():
    num = binary.get()
    print(num, end="")