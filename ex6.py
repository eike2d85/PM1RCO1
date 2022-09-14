import numpy as np

sigma_x = 4
sigma_y = 2
tau_xy = -3
glob_ten = [[sigma_x],[sigma_y],[tau_xy]]
glob_ten = np.matrix(glob_ten)

ang = 30
ang = ang*180/np.pi
c = np.cos(ang)
s = np.sin(ang)
T =  [[c**2, s**2, 2*s*c],[s**2, c**2, -2*s*c],[-s*c, s*c, (c**2-s**2)]]
T = np.matrix(T)
# T_inv = np.linalg.inv(T)

loc_ten = np.matmul(T,glob_ten)
print('Tensões Locais [MPa]:\n', loc_ten)