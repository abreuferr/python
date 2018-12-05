# importar a classe Veiculo do arquivo veiculo.py
from veiculo import Veiculo

# classe main()
def main():
    veiculo1 = Veiculo('carro', 'ferrari', 'vermelho', 280)
    veiculo2 = Veiculo('caminhao', 'ford', 'preto', 195)

    veiculo1.velocidade(200)
    veiculo2.velocidade(200)

# main()
main()