q1 = input("SURVEY Are you interested in computer science? (y/n): ").lower()
q2 = input("Do you like playing computer games? (y/n): ").lower()
q3 = input("Do you have an Instagram account? (y/n): ").lower()

if q1 == "y":
    print("SURVEY RESULTS Interested in computer science: Yes")
else:
    print("SURVEY RESULTS Interested in computer science: No")
if q2 == "y":
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")
if q3 == "y":
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account:  No")