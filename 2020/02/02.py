from sympy.ntheory.generate import prevprime
from sympy import sieve

delivered = 0
counter = 0
tot_gifts = 5433000


while counter < tot_gifts:
    if '7' in str(counter):
        if counter in sieve:
            counter += counter + 1
        else:
            counter = counter + prevprime(counter)
            counter += 1
    else:
        counter += 1
        delivered += 1
print(delivered)
