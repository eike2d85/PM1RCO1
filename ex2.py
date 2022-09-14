import numpy as np

C=[[-0.67308, -1.8269, -1.0577, 0, 0, 0],[-1.8269, -0.67308, -1.4423, 0, 0, 0],[-1.0577, -1.4423, 0.48077, 0, 0, 0],[ 0, 0, 0, 4, 0, 0],[ 0, 0, 0, 0, 2, 0],[0, 0, 0, 0, 0, 1.5]]
# Em GPa
e1 = 1
e2 = 3
e3 = 2
gamma23 = 0
gamma31 = 5
gamma12 = 6
# Em um/m

e = [[e1], [e2], [e3], [gamma23], [gamma31], [gamma12]]

e = np.matrix(e)
C = np.matrix(C)

sigma = np.matmul(C,e)
print('Tensões [GPa]:\n', sigma)

S = np.linalg.inv(C)
print('Matriz de Flexibilidade [1/GPa]:\n', S)

# Constantes de engenharia
E1 = 1/S.item(0)
E2 = 1/S.item(7)
E3 = 1/S.item(14)
G23 = 1/S.item(21)
G31 = 1/S.item(28)
G12 = 1/S.item(35)
v12 = -E1*S.item(1)
v13 = -E1*S.item(2)
v23 = -E2*S.item(8)
print('Constantes de engenharia:')
print('E1 [GPa]:', E1)
print('E2 [GPa]:', E2)
print('E3 [GPa]:', E3)
print('G23 [GPa]:', G23)
print('G31 [GPa]:', G31)
print('G12 [GPa]:', G12)
print('v12:', v12)
print('v13:', v13)
print('v23:', v23)