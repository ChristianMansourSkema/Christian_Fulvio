# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-18 09:23, in .

**Me:** what is the difference between a list and a tuple

**Tutor:**

A list can be changed after it is created (mutable), whereas a tuple cannot be changed (immutable).

```python
def collection_info(coll):
    """
    Return a short description of the collection.
    TODO: Fill in the return statement so it reports:
          - the type of `coll` (list or tuple)
          - the number of elements
    """
    # Example toy data you can test with:
    # my_list = ['alpha', 'beta']
    # my_tuple = ('alpha', 'beta')
    # print(collection_info(my_list))
    # print(collection_info(my_tuple))

    # TODO: replace the line below with your implementation
    return f"Type: {type(coll).__name__}, Length: {len(coll)}"
```

Which built‑in function would you use to turn a mutable list into an immutable tuple?

---
## 2026-10-18 10:14, in .

**Me:** What is the difference between print(str(n) + ". " + msg) and an f-string?

**Tutor:**

String formatting: f-strings embed expressions directly inside a string literal, while concatenation builds a new string with `+`.

```python
def show_message():
    # toy data
    items = [(1, "alpha"), (2, "beta")]
    for n, msg in items:
        # TODO: use concatenation to print "1. alpha"
        print(str(n) + ". " + msg)
        # TODO: use an f-string to print the same line
        print(f"{n}. {msg}")
```

Which of the two `print` statements uses an f-string to embed the variables?

---
## 2026-10-18 16:22, in .

**Me:** What does round(x, y) do

**Tutor:**

`round(x, y)` returns the value of x rounded to y decimal places.

```python
def demo_round():
    # toy data
    numbers = [3.14159, 2.71828, 1.2345]
    # TODO: pick an index and assign the corresponding value to x
    x = numbers[0]          # e.g., change 0 to 1 or 2
    # TODO: set y to the number of decimal places you want
    y = 2
    rounded = round(x, y)
    print(f"Original: {x}, Rounded to {y} decimals: {rounded}")

# TODO: call demo_round() to run the example
```

If you set `x = numbers[1]` and `y = 3`, what will the printed rounded value be?

---
## 2026-10-18 16:23, in .

**Me:** Why does float("70,5") fail, and how could I accept a comma as decimal separator?

**Tutor:**

`float()` expects a string that uses a dot as the decimal separator, so `"70,5"` raises a `ValueError`.  

```python
def parse_number(text):
    # toy data
    samples = ["12,3", "45.6", "78,9"]
    # TODO: choose an index to pick a sample string
    raw = samples[0]          # change 0 to 1 or 2
    # Replace a comma with a dot so float() can understand it
    cleaned = raw.replace(",", ".")
    # Convert to a float
    value = float(cleaned)
    print(f"Original: {raw} → Cleaned: {cleaned} → Float: {value}")

# TODO: call parse_number() to see the result
```

Which string method do we use to turn the comma into a dot before calling `float()`?
