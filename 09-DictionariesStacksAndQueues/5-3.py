paragraph = "cat dog mouse cat rat cat mouse"
paragraph = paragraph.split()

dic = {}

for i in paragraph:
    if i in dic.keys():
        dic[i] = dic[i] + 1 
    else:
        dic[i] = 1

for keys in dic:
    print(f"{keys}: {dic[keys]}")