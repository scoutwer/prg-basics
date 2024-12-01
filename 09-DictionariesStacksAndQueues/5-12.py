import json
# Read the contents of the json file
with open("vote.json" ,'r') as file:
    votes = json.load(file)

# Vote for a person
person_name = input('Name of the person you are voting for: ').lower().strip()
if person_name in votes.keys():
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open("vote.json", 'w') as file:
    json.dump(votes,file)
