# version code 988
# Please fill out this stencil and submit using the provided submission script.

from vecutil import *
from matutil import *
from GF2 import one
from solver import solve



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    result = True
    cur_pos = -1
    for r in A:
      if result is not True:
        break
      for i in range(len(r)):
        if i <= cur_pos:
          if r[i] is not 0:
            result = False
            break
        else:
          cur_pos = i
          if r[i] is not 0:
            break
    return result


## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
      row = rowlist[j]
      for c in label_list:
        if rowlist[j][c] is not 0:
          x[c] = (b[j] - x*row)/row[c]
          break
    return x



## Problem 6
D6 = {'A','B','C','D'}
rowlist = [Vec(D6, {'A':one, 'B':one, 'D':one}), Vec(D6, {'B':one}), Vec(D6,{'C':one}), Vec(D6,{'D':one})]    # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one, one, 0, 0]          # Provide as a list


## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
def project_along(b, a):
  sigma = (b*a)/(a*a) if a*a > 1e-20 else 0
  print("b*a = ",b*a, "a*a = ", a*a)
  return sigma * a
def project_orthogonal_1(b, a):
  return b - project_along(b, a)

#print(project_along(list2vec([2,3]),list2vec([1,2])))
#print(project_along(list2vec([1.414,1,1.732]),list2vec([0,1,0])))
#print(project_along(list2vec([7,2,5,0]),list2vec([-3,-2,-1,4])))
closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

print(project_along(list2vec([2,1]),list2vec([3,0])))
print(project_orthogonal_1(list2vec([2,1]),list2vec([3,0])))
print(project_along(list2vec([1,1,4]),list2vec([1,2,-1])))
print(project_orthogonal_1(list2vec([1,1,4]),list2vec([1,2,-1])))
print(project_along(list2vec([1,1,4]),list2vec([3,3,12])))
print(project_orthogonal_1(list2vec([1,1,4]),list2vec([3,3,12])))
project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-1/6,-2/6,1/6]
projection_orthogonal_2 = [7/6,4/3,23/6]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

