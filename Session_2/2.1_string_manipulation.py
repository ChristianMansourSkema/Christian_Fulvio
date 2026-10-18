"""Exercise 2.1: Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one sentence typed by the user, as text.
# 2. Process: the sentence is cleaned of the spaces around it, then four
#    string methods each build a NEW version of it. The original is never changed.
# 3. Out: the original, then four lines, one per transformation.
#    repr() shows the quotes, so the spaces at both ends become visible.
# 4. My four transformations, and when each is useful:
#    - strip(): clean what someone typed in a form, "  Paris " becomes "Paris".
#    - lower(): compare without caring about capitals, e.g. spot that
#      "Jean@Mail.com" and "jean@mail.com" are the same email in a customer list.
#    - title(): display names or headings nicely, "jean dupont" -> "Jean Dupont".
#    - lower() + replace(" ", "-"): turn a title into a web address or file name,
#      "Winter Sale 2026" -> "winter-sale-2026", no spaces or capitals to break a link.


# Your code below

sentence = input("Type a sentence: ")

# Every transformation starts from the cleaned version, so the spaces
# around the sentence do not end up in the results
clean = sentence.strip()

print("original :", repr(sentence))
print("strip()  :", repr(clean))
print("lower()  :", repr(clean.lower()))
print("title()  :", repr(clean.title()))
print("slug     :", repr(clean.lower().replace(" ", "-")))
