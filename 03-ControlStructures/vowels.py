###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0

# Count vowels in the text
while i < len(text):
    if text[i] in vowels:
        vowel_count += 1
    i = i + 1

print(f"The number of vowels in the text is: {vowel_count}")
