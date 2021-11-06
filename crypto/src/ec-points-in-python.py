# antes de executar o código abaixo, é necessário importar
# o pacote tinyec no python. para isso, basta
# executar o comando abaixo.
#
# pip install tinyec

# importando biblioteca
from tinyec.ec import SubGroup, Curve

# definir os grupos da ecc
field = SubGroup(p=17, g=(15, 13), n=18, h=1)
curve = Curve(a=0, b=7, field=field, name='p1707')

# exibir a equacao que esta sendo utilizada
# curve: "p1707" => y^2 = x^3 + 0x + 7 (mod 17)
print('curve:', curve)

# loop 
for k in range(0, 25):
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")