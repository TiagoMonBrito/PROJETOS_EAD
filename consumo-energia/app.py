#custo fixo pra cada kwH
custo = 0.50

#entrada do usuario
eletronico = input("insira o nome de um eletrodomestico seu: ")
eletronico = eletronico.upper()

potencia = int(input("agora insira a potencia em watts desse eletrodomestico: "))

consumoHoras = int(input("perfeito, agora diga quantas horas  por dia aproximadamente voce utiliza esse aparelho: "))

#processamento
consumomensal = (potencia * consumoHoras * 30) / 1000

gastomensal = (consumomensal * custo)

#saida
print(f"""O seu eletronico: {eletronico}, consome por mes aproximadamente um total de {consumomensal} kWh!
Ao todo no mês voce gasta aproximadamente {gastomensal}R$ apenas com esse eletronico!""")