from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

from echelon import *

def gcd(x,y): return x if y == 0 else gcd(y, x % y)

'''
rint = 93687235698234590245807568924595
sint = 2458764568723576146856987245756
tint = 760838450985630913796469842084
aint = rint * sint
bint = sint * tint
dint = gcd(aint, bint)
print("common denom = ", dint)
print("a divisible = ", aint % dint)
print("b divisible = ", bint % dint)
print("d > s,", dint, sint)
'''
'''
N = 367160330145890434494322103
aint = 67469780066325164
bint = 9429601150488992
print("aint * aint - bint * bint % N", (aint * aint - bint * bint)%N)
print("aint-bint % N", (aint-bint) % N)
print("gcd(aint-bint, N)", gcd(aint-bint, N))
'''
'''
primeset={2, 3, 5, 7, 11, 13}
for x in [12, 154, 2*3*3*3*11*11*13, 2*17, 2*3*5*7*19]:
  print("dumb_factor(x, primeset)",x, dumb_factor(x, primeset))
'''

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return one if i%2 is 1 else 0

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {k:int2GF2(v) for (k,v) in factors})


## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = list()
    rowlist = list()
    i = 2
    while len(roots) < len(primeset)+1:
      x = intsqrt(N) + i
      i += 1
      factorset = dumb_factor(x*x-N, primeset)
      if len(factorset) > 0:
        roots.append(x)
        rowlist.append( make_Vec(primeset,factorset) )
    return (roots, rowlist)

'''
aint = 53*77
bint = 2*3*3*5*13
N = 2419
print("gcd(aint-bint, N)", gcd(aint-bint, N))
aint = 52*67*71
bint = 2*3*3*5*19*23
N = 2419
print("gcd(aint-bint, N)", gcd(aint-bint, N))
'''

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input:
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [roots[i] for i in range(len(roots)) if v[i] != 0]
    a = prod(alist)
    c = prod({x*x - N for x in alist})
    b = intsqrt(c)
    assert b*b == c
    return (a, b)

def get_gcd(N, primeset):
  denom = 1
  cands = find_candidates(N, primeset)
  M = transformation_rows(cands[1], sorted(primeset, reverse=True))
  M_index = len(M)-1
  while denom == 1 and M_index > 0:
    v = M[M_index]
    (aint, bint) = find_a_and_b(v, cands[0], N)
    denom = gcd(aint-bint, N)
    M_index -= 1
  return denom
'''
N = 2419
primeset = primes(32)
print(get_gcd(N, primeset))

N = 2461799993978700679
primeset = primes(10000)
print(get_gcd(N, primeset))
'''
## Task 5

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561
