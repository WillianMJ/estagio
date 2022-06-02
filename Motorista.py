dadosM = dict()
Motorista = list()

qtd = int(input(print("Entre com a quantidade de motorista que irá cadastrar " )))

cont = 0
while cont < qtd:
    dadosM['Cod_mot'] = int(input("Entre com seu codigo "))
    dadosM['Nome'] = (input("Entre com seu nome "))
    dadosM['Telefone'] = int(input("Entre com seu telefone "))
    dadosM['CNH'] = int(input("Entre com sua CNH "))
    Motorista.append(dadosM.copy())
    cont = cont + 1

[print(Cod_mot) for Cod_mot in Motorista]