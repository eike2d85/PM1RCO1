import numpy as np

# Unidirecional vidro/epoxi
Vf = 0.4
Ef = 85 # GPa
Em = 3.4 # GPa
vf = 0.2
vm = 0.3
Gf = Ef/(2*(1+vf))
Gm = Em/(2*(1+vm))
Vm = 1 - Vf
E1_mist = Vf*Ef + Vm*Em
E2_mist = 1/((Vf/Ef)+(Vm/Em))
v12_mist = vf*Vf + vm*Vm
v21_mist = v12_mist*E2_mist/E1_mist
G12_mist = 1/((Vf/Gf)+(Vm/Gm))

print('Regra das misturas:')
print('E1 [GPa]:', E1_mist)
print('E2 [GPa]:', E2_mist)
print('v12 (Major):', v12_mist)
print('v21 (Minor):', v21_mist)
print('G12 [GPa]:', G12_mist)

E1_ht = Vf*Ef + Vm*Em
e_long = 2
eta_long = ((Ef/Em)-1)/((Ef/Em)+e_long)
E2_ht = Em*((1+(e_long*eta_long*Vf))/(1-(eta_long*Vf)))
v12_ht = vf*Vf + vm*Vm
v21_ht = v12_ht*E2_ht/E1_ht
e_cis = 1
eta_cis = ((Gf/Gm)-1)/((Gf/Gm)+e_cis)
G12_ht = Gm*((1+(e_cis*eta_cis*Vf))/(1-(eta_cis*Vf)))

print('Halphin e Tsai:')
print('E1 [GPa]:', E1_ht)
print('E2 [GPa]:', E2_ht)
print('v12 (Major):', v12_ht)
print('v21 (Minor):', v21_ht)
print('G12 [GPa]:', G12_ht)
