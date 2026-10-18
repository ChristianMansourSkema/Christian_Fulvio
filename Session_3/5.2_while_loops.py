"""Exercise 5.2: Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the customer's answers to "Confirm your order?", typed one at a time.
# 2. Process: each answer is cleaned (spaces removed, put in lowercase) and
#    compared to "yes" and "no". The loop stops on a clear answer, or when
#    the attempts run out. 
# 3. Out: a reminder after each unclear answer, then a summary: the outcome,
#    the number of attempts used.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop: the customer answers "yes" (order confirmed) or "no" (cancelled).
#      "yes", "Yes", " YES " count as the same answer: I remove the spaces and
#      ignore capitals. "y" or "ok" do NOT count: a typo must not confirm
#      a payment.
#    - Limit: 3 attempts. After 3 unclear answers the order is NOT placed.




# Your code below


# The safety limit
MAX_ATTEMPTS = 3

attempts = 0
outcome = f"Order NOT placed: no clear answer after {MAX_ATTEMPTS} attempts."

# The loop cannot run for ever,so it stops at MAX_ATTEMPTS even if the customer never answers clearly
while attempts < MAX_ATTEMPTS:
    raw = input(f"Confirm your order? Type yes or no ({attempts + 1}/{MAX_ATTEMPTS}): ")
    attempts += 1
   

    # remove the spaces around it, then ignore capitals
    answer = raw.strip().lower()

    # break leaves the loop at once: a clear answer ends the questions
    if answer == "yes":
        outcome = "Order confirmed."
        break
    elif answer == "no":
        outcome = "Order cancelled by the customer."
        break
    else:
        print("Please answer with yes or no.")

# The summary, displayed whatever the way the loop ended
print()
print("Summary")
print(f"- {outcome}")
print(f"- Attempts used: {attempts} out of {MAX_ATTEMPTS}")
