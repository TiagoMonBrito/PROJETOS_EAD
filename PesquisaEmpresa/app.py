print("Bem Vindo!")

QuantExelente = 0
QuantRuim = 0

#ENTRADA
for candidato in range(1,6):
  nome = input("insira o seu nome: ")
  idade = int(input("insira agora a sua idade: "))
  avaliação = int(input("nos diga a sua avaliação pessoal sobre a empresa\ndigite 1 para: 'EXCELENTE'\ndigite 2 para: 'BOM'\ndigite 3 para: 'RUIM' "))
  
  #PROCESSAMENTO
  match avaliação:
    case 1:
      avaliação = "EXCELENTE"
      QuantExelente += 1
    case 2:
      avaliação = "BOM"
    case 3:
      avaliação = "RUIM"
      QuantRuim += 1
    case _:
      raise ValueError("apenas digitos entre 1 - 3 apenas!")

#SAIDA
print(f"Obrigado por responder a pesquisa!\nMédia de avaliações:\nEXCELENTE: {QuantExelente}\nRUIM: {QuantRuim}")