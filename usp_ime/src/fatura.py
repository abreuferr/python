# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : fatura do cartao de credito

# inserir os dados
nome_cliente = input("Digite o nome do cliente: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor_fatura = input("Digite o valor da fatura: ")

# exibir o resultado da conversao
print("Olá,", nome_cliente)
print("A sua fatura com vencimento em", dia_vencimento,"de", mes_vencimento, "no valor de R$", valor_fatura, "está fechada.")