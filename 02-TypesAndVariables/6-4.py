###
# A program for displaying detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
name, surname = employee[4:12].split()
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:]}')
print(f'Initials: {name[0] + surname[0]}')