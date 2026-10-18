"""Exercise 5.0: Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number typed by the user, their BMI (e.g. 22.9 from exercise 2.0).
# 2. Process: the text is converted with float(), then compared to the
#    boundaries from the smallest to the largest. The first range that
#    matches decides the message, the others are not checked.
# 3. Out: one message giving the BMI category.
# 4. My ranges, my boundaries, my messages:
#    I use the World Health Organization categories, the reference used by
#    doctors, so the cut-offs are not my opinion.
#    - below 18.5               -> "underweight"
#    - 18.5 up to, not incl. 25 -> "normal weight"
#    - 25 up to, not incl. 30   -> "overweight"
#    - 30 and above             -> "obesity"
#    A value exactly on a boundary goes to the range ABOVE: 18.5 is normal,
#    25 is overweight, 30 is obesity. That is how the WHO defines them.
#    Extra: 0 or less is not a possible BMI, so it gets its own message.


# Your code below


bmi = float(input("Your BMI: "))

# Checked from the smallest to the largest
# a value exactly on a boundary falls through to the next range, the one above
if bmi <= 0:
    print("This is not a possible BMI. Check the value you typed.")
elif bmi < 18.5:
    print(f"BMI {bmi}: underweight. A doctor can check whether this is a concern.")
elif bmi < 25:
    print(f"BMI {bmi}: normal weight.")
elif bmi < 30:
    print(f"BMI {bmi}: overweight.")
else:
    print(f"BMI {bmi}: obesity. A doctor can give advice adapted to you.")
