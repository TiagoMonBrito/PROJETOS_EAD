#valor fixo por cada kwh
custo = 0.5

#entrada do usuario
eletrodomestico = input("insira um eletrodomestico de sua casa: ")
eletrodomestico = eletrodomestico.upper()

potencia = int(input("insira a potencia desse eletronico em watts: "))


usodiario = int(input("insira a quantidade de horas que voce utiliza diariamente desse produto: "))

#processamento
kwhMensal = (potencia * usodiario * 30) / 1000
kwhCusto = kwhMensal * custo

#saida
print(f"""em sua residencia, o aparelho {eletrodomestico} consome por mês um total de {kwhMensal}Kwh de energia!
isso é um consumo de {kwhCusto}R$ por mês""")