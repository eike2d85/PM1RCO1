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
# print('Matriz de rigidez global [MPa]:\n', C_glob)
S_glob = np.linalg.inv(C_glob)
# print('Matriz de fexibilidade global [1/MPa]:\n', S_glob)
def_glob = np.matmul(S_glob,glob_ten)
print('Deformações Globais:\n', def_glob)
loc_ten = np.matmul(T,glob_ten)
print('Tensões Locais [MPa]:\n', loc_ten)
loc_ten_mod = loc_ten
loc_ten_mod.itemset((2),loc_ten.item(2)/2)
def_loc = np.matmul(S_loc,loc_ten_mod)
print('Deformações Locais:\n', def_loc)
sig_max = ((sigma_x + sigma_y)/2)+(((sigma_x - sigma_y)/2)**2 + tau_xy**2)**0.5
sig_min = ((sigma_x + sigma_y)/2)-(((sigma_x - sigma_y)/2)**2 + tau_xy**2)**0.5
print('Tensão Normal Principal 1 [MPa]:', sig_max)
print('Tensão Normal Principal 2 [MPa]:', sig_min)
tau_max = (((sigma_x - sigma_y)/2)**2 + tau_xy**2)**0.5
print('Tensão Cisalhante Principal [MPa]:', tau_max)
e_x = def_glob.item(0)
e_y = def_glob.item(1)
gamma_xy = def_glob.item(2)
e_max = ((e_x + e_y)/2)+(((e_x - e_y)/2)**2 + gamma_xy**2)**0.5
e_min = ((e_x + e_y)/2)-(((e_x - e_y)/2)**2 + gamma_xy**2)**0.5
print('Deformação Normal Principal 1:', e_max)
print('Deformação Normal Principal 2:', e_min)
gamma_max = ((e_x-e_y)**2 + gamma_xy**2)**0.5
print('Deformação Cisalhante Principal:', gamma_xy)