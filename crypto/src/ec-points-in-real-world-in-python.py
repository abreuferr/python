# antes de executar o código abaixo, é necessário importar
# o pacote tinyec no python. para isso, basta
# executar o comando abaixo.
#
# pip install tinyec

# importando biblioteca
from tinyec import registry

curve = registry.get_curve('secp192r1')
print('curve:', curve)

for k in range(0, 10):
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")
    
print("Cofactor =", curve.field.h)

print('Cyclic group order =', curve.field.n)

nG = curve.field.n * curve.g
print(f"n * G = ({nG.x}, {nG.y})")