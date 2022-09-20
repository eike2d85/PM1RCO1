import numpy as np

# Calcular: Fração mássica e densidade do compósito

Vf_vidro = 0.4
Vf_graf = 0.2
rho_m = 1200 #kg/m³
rho_vidro = 2500 #kg/m³
rho_graf = 1800 #kg/m³
Vm = 1-Vf_graf-Vf_vidro

rho_c = rho_m*Vm + rho_vidro*Vf_vidro + rho_graf*Vf_graf
Wf_vidro = rho_vidro*Vf_vidro/rho_c
Wf_graf = rho_graf*Vf_graf/rho_c
Wm = rho_m*Vm/rho_c
print('Fração mássica de fibra de vidro:', Wf_vidro)
print('Fração mássica de fibra de grafite:', Wf_graf)
print('Fração mássica de matriz:', Wm)
print('Densidade do compósito [kg/m³]:', rho_c)
