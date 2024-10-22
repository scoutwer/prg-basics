###
# Functions to read any data type from the keyboard
#
def input_string(message):
    result = input(message)
    return result

def input_integer(message):
    result = int(input(message))
    return result

def input_real(message):
    answer = input(message)
    if answer.isdigit() == True:
        return answer
    else:
        return "This is not a real number"

def input_boolean(message):
    answer = input(message).lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        return "Something went Wrong"

if __name__ == "__main__":
    print()