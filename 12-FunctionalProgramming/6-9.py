dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

arr = list(filter(lambda x: dic[x] > 0, dic))

print("Cities with positive temperatures:", end=" ")
for i in arr:
    print(i,end = " ")
