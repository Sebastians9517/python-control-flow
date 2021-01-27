
# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


def is_a_vowel(c):
    vowels = "aeiouAEIOU"
    if c in vowels:
        print(f"The letter {c} is a vowel.")
    else:
        print(f"The letter {c} is a consonant.")

print(is_a_vowel(input("Please enter a letter from the alphabet (a - z or A - Z): ")))



# Alternatively:

# c = input("Please enter a letter from the alphabet (a - z or A - Z)")

# if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or
#     c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
#     print(f"The letter {c} is a vowel")
# else:
#     print(f"The letter {c} is a consonant")
