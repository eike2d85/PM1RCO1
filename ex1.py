import numpy as np

def stiff(E1, E2, E3, v12, v23, v31, G12,G23, G31):

    C=np.matrix('1 2; 3 4')

    return C