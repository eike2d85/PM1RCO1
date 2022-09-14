import numpy as np

ksi_MPa = 6.894760
C = [[5.681, 0.3164, 0],[0.3164, 1.217, 0],[0, 0, 0.6006]]
C = np.matrix(C)
C = C*ksi_MPa

S = np.linalg.inv(C)

E1 = 1/S.item(0)
E2 = 1/S.item(4)
G12 = 1/S.item(8)
v12 = -E1*S.item(1)
print('Constantes de engenharia:')
print('E1 [GPa]:', E1)
print('E2 [GPa]:', E2)
print('G12 [GPa]:', G12)
print('v12:', v12)
