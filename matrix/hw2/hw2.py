# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one



## Problem 1
def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [v for v in veclist if k not in v.f or v.f[k] is 0]

def vec_sum(veclist, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    dic = dict()
    for k in D:
        key_sum = sum([v.f[k] if k in v.f else 0 for v in veclist])
        if key_sum is not 0:
            dic[k] = key_sum
    return Vec(D, dic)

def vec_select_sum(veclist, k, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist, k), D)


## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    return [Vec(vecdict[m].D, {k:vecdict[m].f[k]/m for k in vecdict[m].f.keys()}) for m in vecdict.keys()]

def scale_up_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 27}), Vec({1,2,4},{1: 5, 2: 10, 4: 40})]
    True
    '''
    return [Vec(vecdict[m].D, {k:vecdict[m].f[k]*m for k in vecdict[m].f.keys()}) for m in vecdict.keys()]



## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    gf2_opt = gen_GF2(len(L))
    arr = list()
    for x in gf2_opt:
        sub_arr = list()
        for y in range(len(x)):
            sub_arr.append(scale_up_vecs({ x[y]:L[y] })[0])
        arr.append(vec_sum(sub_arr, D))
    return arr

def gen_GF2(length, lists=[]):
    if len(lists) is 0:
        lists = [[]]

    for i in range(len(lists)):
        l = lists[i][:]
        lists[i].append(0)
        l.append(one)
        lists.append(l)

    if len(lists[0]) is length:
        return lists
    else:
        return gen_GF2(length, lists)

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6

is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
