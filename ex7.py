import numpy as np
from ex4 import flex_stiff_plano

# Tensões gobais em MPa
sigma_x = 4
sigma_y = 2
tau_xy = -3
glob_ten = [[sigma_x],[sigma_y],[tau_xy]]
glob_ten = np.matrix(glob_ten)

# Propriedades da lâmina em MPa
E1 = 204000
E2 = 18500
v12 = 0.23
G12 = 5590
Vf = 0.5 # fração volumétrica

# Matrizes de rigidez e flexibilidade no sistema local 
C_loc, S_loc = flex_stiff_plano(E1, E2, v12, G12)


ang = 60
ang = ang*180/np.pi
c = np.cos(ang)
s = np.sin(ang)
T =  [[c**2, s**2, 2*s*c],[s**2, c**2, -2*s*c],[-s*c, s*c, (c**2-s**2)]]
T = np.matrix(T)
T_inv = np.linalg.inv(T)
R = [[1, 0, 0],[0, 1, 0],[0, 0, 2]]
R = np.matrix(R)
R_inv = np.linalg.inv(R)
C_tmp1 = np.matmul(T_inv,C_loc)
C_tmp2 = np.matmul(C_tmp1,R)
C_tmp3 = np.matmul(C_tmp2,T)
C_glob = np.matmul(C_tmp3,R_inv)
print('Matriz de rigidez global [MPa]:\n', C_glob)

loc_ten = np.matmul(T,glob_ten)
print('Tensões Locais [MPa]:\n', loc_ten)