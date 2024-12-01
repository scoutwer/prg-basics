def f(word):
    stack = []
    result = ""
    for i in word:
        stack.append(i)
    while stack:
        result += stack.pop()

    return result


print(f("CHUJ MI W DUPE"))
