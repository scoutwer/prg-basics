###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("number of correct tasks: "))
test_passed = False

if tasks_ok >= total_tasks*0.5 :
    test_passed = True

if test_passed == True:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')