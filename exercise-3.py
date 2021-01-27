# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dog_age_human_years = int(input("Please enter your dog's age (in normal human years): "))

if dog_age_human_years <= 2:
    dog_age_dog_years = (dog_age_human_years * 10)
    print(f"The dog age in dog years is: {dog_age_dog_years}")
else:
    dog_age_dog_years = (2*10) + ((dog_age_human_years - 2) * 7)
    print(f"The dog age in dog years is: {dog_age_dog_years}")
