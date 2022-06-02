carro = dict()
frota = list()

qtd = int(input(print("Entre com a quantidade de carros que deseja cadastrar " )))

cont = 0
while cont < qtd:
    carro['Placa'] = int(input("Entre com a placa "))
    carro['marca'] = (input("Insira a marca do carro "))
    carro['veículo'] = int(input("Insira o modelo do veículo "))
    carro['km_troca_oleo'] = int(input("Insira a quilometragem da troca de óleo "))
    frota.append(carro.copy())
    cont = cont + 1

[print(Placa) for Placa in frota]