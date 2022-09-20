import numpy as np

Wf = 0.4
Wm_A = 0.3
Wm_B = 0.3
rho_f = 1200 #kg/m³
rho_A = 2600 #kg/m³
rho_B = 1700 #kg/m³
rho_c = 1/((Wm_A/rho_A)+(Wm_B/rho_B)+(Wf/rho_f))
Vf = Wf*rho_c/rho_f
print('Fração volumétrica de fibra:', Vf)
print('Densidade do compósito [kg/m³]:', rho_c)
