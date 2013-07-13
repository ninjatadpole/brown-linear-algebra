from plotting import plot

def addn(v,w): return [v[i]+w[i] for i in range(len(v))]

def scalar_vector_mult(alpha, v): return [alpha*x for x in v]

def line(orig, dest, density=50):
    """ return the coordinates for points on the line between orig and dest, with density entries """
    return[addn(scalar_vector_mult(i/density, dest), scalar_vector_mult((1-i/density), orig)) for i in range(density+1)]

plot(line([2,1],[-2,2]))

