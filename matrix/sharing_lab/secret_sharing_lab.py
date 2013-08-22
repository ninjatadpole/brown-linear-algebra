# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import *
from itertools import combinations



## Problem 1
def randGF2(i): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
  u = list2vec([randGF2(i) for i in range(6)])
  while a0 * u != s or b0 * u != t:
    u[random.randint(0,5)] = randGF2(0)
  return u

'''
print(choose_secret_vector(0,0))
print(choose_secret_vector(0,one))
print(choose_secret_vector(one,0))
print(choose_secret_vector(one, one))
'''

## Problem 2
#def is_independent(L):
#    return len(L) is rank(L)

vecs = [(a0, b0)]
test_vecs = list()

for i in range(4):
  are_independent = False
  while are_independent is False:
    a_vec = choose_secret_vector(randGF2(i), randGF2(i))
    b_vec = choose_secret_vector(randGF2(i), randGF2(i))
    if (a_vec,b_vec) not in vecs:
      test_vecs = vecs[:]
      test_vecs.append((a_vec,b_vec))
      selection = min(3,len(test_vecs))
      are_independent = all(is_independent(list(sum(x,()))) for x in combinations(test_vecs,3))
  vecs.append((a_vec,b_vec))

for i in range(len(vecs)):
  print(i)
  print(vecs[i][0])
  print(vecs[i][1])


# Give each vector as a Vec instance
secret_a0 = list2vec([one, one, 0, one, 0, one])
secret_b0 = list2vec([one, one, 0, 0, 0, one])
secret_a1 = list2vec([one, one, one, 0, 0, 0])
secret_b1 = list2vec([one, one, one, 0, 0, one])
secret_a2 = list2vec([one, 0, 0, 0, 0, 0])
secret_b2 = list2vec([0, one, 0, one, one, 0])
secret_a3 = list2vec([one, 0, one, 0, one, one])
secret_b3 = list2vec([one, 0, one, one, 0, one])
secret_a4 = list2vec([0, one, one, one, one, one])
secret_b4 = list2vec([one, 0, 0, one, 0, one])

