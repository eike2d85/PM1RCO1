import numpy as np

# vidro/epoxi
Vf_vidro = 0.7
Ef_vidro = 85 # GPa
Em = 3.4 # GPa
Vm = 1 - Vf_vidro
E1_vidro = Ef_vidro*Vf_vidro + Em*Vm
print('E1 [GPa]', E1_vidro)
# grafite/epoxi
Ef_graf = 230 # GPa
Vf_graf = (E1_vidro - Em*Vm)/Ef_graf
print('Fração volumétrica de fibra para Grafite/Epóxi:', Vf_graf)

