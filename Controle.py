rota = dict()
rotas = list()

qtd = int(input(print("Entre com a quantidade de rotas que deseja cadastrar " )))

cont = 0
while cont < qtd:
    rota['Cod_mot'] = int(input("Entre com  codigo do motisra a serviço "))
    rota['placa'] = (input("Entre a placa do carro a serviço "))
    rota['data_saida'] = int(input("Insira data de saída "))
    rota['hora_saida'] = int(input("Insira a hora de Saida "))
    rota['km_saida'] = int(input("Insira o Km de saída "))
    rota['destino'] = (input("Entre com o Destino "))
    rota['data_retorno'] = int(input("Insira data de retorno "))
    rota['hora_retorno'] = int(input("Insira a hora de retorno "))
    rota['km_percorrido'] = int(input("Insira o Km percorrido "))
    rota['km_retorno'] = int(input("Insira o Km de retorno "))
    rotas.append(rota.copy())
    cont = cont + 1

[print(Cod_mot) for Cod_mot in rotas]