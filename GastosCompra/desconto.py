#entrada do usuario com o valor da compra total
print("bem vindo, este programa tem o intuito de te ajudar com o valor de suas compras!")

compra = int(input("insira o valor total da sua compra: "))
desconto = 0

#processamento dos valores do usuario, a partir de uma condicional
if compra >= 300:
  desconto = 0.15
  compra = compra - (compra*desconto)
  
elif compra >= 200:
  desconto = 0.10
  compra = compra - (compra*desconto)
  
elif compra < 200:
  desconto = 0.05
  compra = compra - (compra*desconto)

#saida com os valores do desconto e o valor final a pagar
print(f"sua compra teve um total de {desconto*100}% apenas em descontos! o preço total foi de: {compra}R$")