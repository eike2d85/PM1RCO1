import numpy as np

# vidro/epoxi unidirecional
Vf = 0.4
Ef = 85 # GPa
Em = 3.4 # GPa
Vm = 1 - Vf
E1 = Ef*Vf + Em*Vm
print('E1 [GPa]', E1)