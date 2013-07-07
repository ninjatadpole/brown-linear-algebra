# maximum 3 digit numbers
base = 2
digits = {0,1,2,3,4,5,6,7,8,9}
{x*base**0 + y*base**1 + z*base**2 for x in digits for y in digits for z in digits if x<base and y<base and z<base}

# find intersection without &
S = {1,2,3,4}
T = {3,4,5,6}
{x for x in S for y in T if x=y}
# or
{x for x in S if x in T}

# 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
sum([sum(x) for x in LofL])

# 13
[[x,y] for x in ['A','B','C'] for y in [1,2,3]]

# 14
S = {-4,-2,1,2.5,0}
[(x,y,z) for x in S for y in S for z in S if x+y+z==0]

# 15
S = {-4,-2,1,2.5,0}
[(x,y,z) for x in S for y in S for z in S if x+y+z==0 and x!=0 and y!=0 and z!=0]

# 16
[(x,y,z) for x in S for y in S for z in S if x+y+z==0 and x!=0 and y!=0 and z!=0][0]

# 19
L = ['A','B','C','D','E']
list(zip(range(5), L))

# 20
[x+y for (x,y) in zip([10,25,40],[1,15,20])]

# 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger',
'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
[dlist[x][k] for x in dlist]
[x[k] for x in dlist]

# 23
{x:x*x for x in range(100)}

# 24
D = {'red','white','blue'}
{x:x for x in D}

# 25
base = 10
digits = set(range(10))
{(x*base**0 + y*base**1 + z*base**2):[z, y, x] for x in digits for y in digits for z in digits if x<base and y<base and z<base}

# 26
d = {0:1000.0, 3:990, 1:1200.50}
L = ['Larry', 'Curly', '', 'Moe']
{L[x]:d[x] for (x,y) in d.items()}
