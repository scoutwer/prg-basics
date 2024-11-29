translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

list  = translations.keys()
user_input = input("Enter a word: ")

if user_input in list:
    print(translations[user_input])
else:
    print("translation is unavailable")
