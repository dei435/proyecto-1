capital = int(input("Ingrese su capital: "))
capital_del_cliente = 125
nivel_despecho = input("Ingrese el nivel de despecho (Sabroson, Lloroso o Quien soy?): ")

niveles = {"Sabroson": 50, "Lloroso": 80, "Quien soy?": 120}
bebidas = {"Serenata": {"costo": 10, "valor_felicidad": 2},
           "Alpargata": {"costo": 15, "valor_felicidad": 5},
           "Agua miel": {"costo": 25, "valor_felicidad": 10},
           "Olimpo": {"costo": 50, "valor_felicidad": 20},
           "Que te perdone Dios": {"costo": 120, "valor_felicidad": 80}}

cantidad_bebidas = {}
valor_total_felicidad = 0

for bebida, datos in bebidas.items():
    while capital >= datos["costo"] and valor_total_felicidad < niveles[nivel_despecho]:
        capital -= datos["costo"]
        valor_total_felicidad += datos["valor_felicidad"]
        if bebida in cantidad_bebidas:
            cantidad_bebidas[bebida] += 1
        else:
            cantidad_bebidas[bebida] = 1


if valor_total_felicidad >= niveles[nivel_despecho]:
    print("El cliente alivio sus penas, se le sirvieron:")
    for bebida, cantidad in cantidad_bebidas.items():
        print("- {} botella(s) de {}".format(cantidad, bebida))
else:
    print("El cliente no pudo aliviar sus penas, no cuenta con el capital necesario.")
    
