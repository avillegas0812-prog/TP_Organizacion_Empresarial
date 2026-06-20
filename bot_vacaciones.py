print("================================")
print("BOT DE GESTION DE VACACIONES")
print("================================")

legajos = {
    "1001": {"nombre": "Juan Perez", "dias": 15},
    "1002": {"nombre": "Maria Lopez", "dias": 10},
    "1003": {"nombre": "Ana Garcia", "dias": 20},
    "1004": {"nombre": "Pedro Gomez", "dias": 5}
}

legajo = input("Ingrese su numero de legajo: ")

if legajo in legajos:

    nombre = legajos[legajo]["nombre"]
    dias_disponibles = legajos[legajo]["dias"]

    print("\nBienvenido", nombre)
    print("Dias disponibles:", dias_disponibles)

    opcion = input(
        "\nSeleccione una opcion:\n"
        "1 - Consultar dias disponibles\n"
        "2 - Solicitar vacaciones\n"
        "Opcion: "
    )

    if opcion == "1":

        print("\nPosee", dias_disponibles, "dias disponibles.")

    elif opcion == "2":

        try:

            dias_solicitados = int(
                input("Ingrese la cantidad de dias solicitados: ")
            )

            if dias_solicitados <= 0:

                print("Cantidad invalida.")

            elif dias_solicitados <= dias_disponibles:

                print("\nSolicitud aprobada.")
                print("Dias restantes:",
                      dias_disponibles - dias_solicitados)

            else:

                print("\nSolicitud rechazada.")
                print("No posee saldo suficiente.")

        except ValueError:

            print("Debe ingresar un numero valido.")

    else:

        print("Opcion incorrecta.")

else:

    print("Legajo inexistente.")