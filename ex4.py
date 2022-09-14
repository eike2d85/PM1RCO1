import numpy as np

def flex_stiff_plano(E1, E2, v12, G12):
    S = np.zeros((3,3))
    v21 = v12*(E2/E1)
    
    s11 = 1/E1
    s22 = 1/E2
    s12 = -v12/E1

    s21 = -v21/E2
    s66 = 1/G12

    S.itemset((0,0),s11)
    S.itemset((1,1),s22)
    S.itemset((0,1),s12)
    S.itemset((1,0),s21)
    S.itemset((2,2),s66)

    C = np.linalg.inv(S)
    
    return C,S


# Propriedades em GPa
E1 = 204
E2 = 18.5
v12 = 0.23
G12 = 5.59

Vf = 0.5 #fração volumétrica

C,S = flex_stiff_plano(E1, E2, v12, G12)
print('Matriz de Rigidez: [GPa]\n', C)
print('Matriz de Flexibilidade: [1/Gpa]\n', S)