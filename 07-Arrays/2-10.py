###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
i = 0
for res in test_results:
    if res == True:
        i = i + 1

# calculates the number of incorrect answers
incorrect_answers = question_number - i
# calculates the percentage of correct answers
precentage = i / question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', i)
print('Number of incorrect answers:', incorrect_answers)
print('Percantage of correct answers:', precentage)