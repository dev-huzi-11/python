# ************************************** FROZEN SET **************************************

# A frozen set is an immutable version of a set. Once created, it cannot be changed (no adding or removing elements).

frozen_A = frozenset([1, 2, 3, 4, 5])
print(frozen_A)

# frozen_A.add(6)  # ❌ This will cause an error because frozen sets are immutable


# OPERATIONS 
frozen_B = frozenset([3, 4, 5, 6])

print(frozen_A | frozen_B)  # Union
print(frozen_A & frozen_B)  # Intersection
print(frozen_A - frozen_B)  # Difference
print(frozen_A ^ frozen_B)  # Symmetric Difference
