def count(letter, text):
    result = 0 
    for i in text:
        if i == letter:
            result = result +  1
    return result


print(f"The number of letter 'e': {count("e", "You never get a second chance to make a first impression")}")