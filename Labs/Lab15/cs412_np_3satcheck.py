"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

from itertools import product

# PART B
# B.1
all_assignments = list(product([False, True], repeat=3))

def truth(x1, x2, x3):
    return (
        (not x1 or not x2 or not x3) and
        (not x1 or not x2 or x3) and
        (not x1 or x2 or not x3) and
        (not x1 or x2 or x3) and
        (x1 or not x2 or not x3) and
        (x1 or not x2 or x3) and
        (x1 or x2 or not x3) and
        (x1 or x2 or x3)
        )

def modified_truth(x1, x2, x3):
    return (
        (not x1 or not x2 or not x3) and
        (not x1 or not x2 or x3) and
        (not x1 or x2 or not x3) and
        (not x1 or x2 or x3) and
        (x1 or not x2 or not x3) and
        (x1 or not x2 or x3) and
        (x1 or x2 or not x3)
        # (x1 or x2 or x3)
        )

# B.2
unsatisfiable = True
for assignment in all_assignments:
    x1, x2, x3 = assignment
    if truth(x1, x2, x3):
        print(f"Satisfiable assignment found: x1={x1}, x2={x2}, x3={x3}")
        unsatisfiable = False

if unsatisfiable:
    print("The 3SAT sentence is unsatisfiable for all possible assignments.")

# B.3
for assignment in all_assignments:
    x1, x2, x3 = assignment
    if modified_truth(x1, x2, x3):
        print(f"Satisfiable assignment found for modified 3SAT: x1={x1}, x2={x2}, x3={x3}")