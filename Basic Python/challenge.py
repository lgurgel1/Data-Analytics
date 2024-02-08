valores = []

quantidade_total_cd = int(input("Digite a quantidade total de CDS: "))
for i in range(0,quantidade_total_cd):
    valor_unitario_cd = float(input(f"Agora, digite o valor do CD {i+1}: "))
    valores.append(valor_unitario_cd)

soma = 0
for valor in valores:
    soma += valor
print(f'O valor total investido nos CDs foi de R${soma:.2f}')

media = soma / quantidade_total_cd
print(f'O valor médio gasto em cada um dos CDs foi de R${media:.2f}')