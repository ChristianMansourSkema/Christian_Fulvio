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
