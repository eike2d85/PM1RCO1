import numpy as np

def flex_stiff(E1, E2, E3, v12, v23, v31, G12,G23, G31):
    S = np.zeros((6,6))
    v13 = v31*(E1/E3)
    v32 = v23*(E3/E2)
    v21 = v12*(E2/E1)
    
    s11 = 1/E1
    s22 = 1/E2
    s33 = 1/E3
    s12 = -v12/E1
    s13 = -v13/E1
    s23 = -v23/E2
    s21 = -v21/E2
    s31 = -v31/E3
    s32 = -v32/E3
    s44 = 1/G23
    s55 = 1/G31
    s66 = 1/G12

    S.itemset((0,0),s11)
    S.itemset((1,1),s22)
    S.itemset((2,2),s33)
    S.itemset((0,1),s12)
    S.itemset((0,2),s13)
    S.itemset((1,0),s21)
    S.itemset((2,0),s31)
    S.itemset((2,1),s32)
    S.itemset((1,2),s23)
    S.itemset((3,3),s44)
    S.itemset((4,4),s55)
    S.itemset((5,5),s66)

    C = np.linalg.inv(S)
    
    return C,S

ksi_MPa = 6.894760 # converte de ksi para MPa
E1 = 4 * ksi_MPa
E2 = 3 * ksi_MPa
E3 = 3.1 * ksi_MPa
v12 = 0.2
v23 = 0.4
v31 = 0.6
G12 = 6 * ksi_MPa
G23 = 7 * ksi_MPa
G31 = 2 * ksi_MPa

C,S = flex_stiff(E1, E2, E3, v12, v23, v31, G12,G23, G31)

print('Matriz de Rigidez: [GPa]\n', C)
print('Matriz de Flexibilidade: [1/Gpa]\n', S)