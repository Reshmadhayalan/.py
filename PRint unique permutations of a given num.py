from itertools import permutations
def unique_permutations (num):
  digits = str(num)
  perms= set(permutations(digits))
  for p in sorted(perms):
    print (' '.join(p))

num= 122
unique_permutations(num)
