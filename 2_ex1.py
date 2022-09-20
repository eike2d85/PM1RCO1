import numpy as np

Wf = 0.75

# Da tabela:
rho_f = 2500 #kg/m³
rho_m = 1200 #kg/m³

Wm = 1-Wf
rho_c = 1/((Wf/rho_f)+(Wm/rho_m))

Vf = Wf*rho_c/rho_f
Vm = Wm*rho_c/rho_m
print('Fração volumétrica de fibra:', Vf)
print('Fração volumétrica de matriz:', Vm)
print('Densidade do compósito [kg/m³]:', rho_c)
