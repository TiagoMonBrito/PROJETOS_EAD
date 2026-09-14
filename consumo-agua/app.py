
imovel = int(input("INSIRA O SEU TIPO DE IMOVEL: 1- CASA ; 2- APARTAMENTO ; 3- COMERCIAL "))
ConsumoAgua = int(input("INSIRA AGORA A QUANTIDADE DE AGUA QUE É UTILIZADA POR MÊS EM SEU IMOVEL, EM METROS CUBICOS: "))

if imovel == 3:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif imovel == 2 and ConsumoAgua <= 10:
    print("Consumo econômico - excelente uso de agua!")

elif (imovel == 1 or imovel == 2) and ConsumoAgua <= 25:
    print("Consumo Moderado - dentro do limite residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

