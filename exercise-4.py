# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Please enter the length of the three sides of a triangle next.")
side_a = int(input("Please enter side a: "))
side_b = int(input("Now please enter side b: "))
side_c = int(input("And lastly, please enter side c: "))

if ((side_a == side_b) and (side_b == side_c)):
    print(f"A triangle with sides {side_a}, {side_b}, and {side_c} is equilateral.")
elif ((side_a != side_b) and (side_b != side_c) and (side_a != side_c)):
    print(f"A triangle with sides {side_a}, {side_b} and {side_c} is an scalene triangle.")
else:
    print(f"A triangle with sides {side_a}, {side_b} and {side_c} is an isosceles triangle.")
