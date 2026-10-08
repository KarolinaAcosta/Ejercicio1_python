from datetime import datetime


def check_fields(linea, numero_linea):
    fields = linea.split(",")   #splitdivide un texto usando la coma (,) como separador.

    if len(fields) != 4: #si la cantidad de fields es diferente de 4
        if linea == "":
            print("La línea", numero_linea, "está vacía y no cumple con los 4 campos.")
        else: 
            print("La línea", numero_linea, "no cumple: debe tener exactamente 4 campos:", linea)
        return

    fecha, bot, ejecucion, tiempo = fields #como la cantidad de fields es 4, se asignan a las variables corespondientes

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("La línea", numero_linea, "no cumple: la fecha debe tener formato año-mes-día:", linea)
        return

    if (bot != "bot_facturas" and bot != "bot_nomina"
            and bot != "bot_cartera"):
        print("La línea", numero_linea, "no cumple: el bot no es válido:", linea)
        return

    if ejecucion != "exitosa" and ejecucion != "fallida":
        print("La línea", numero_linea, "no cumple: la ejecución debe ser exitosa o fallida:", linea)
        return

    if not tiempo.isdigit():
        print("La línea", numero_linea, "no cumple: el tiempo debe ser un número entero:", linea)
        return

    print("La línea", numero_linea, "cumple con los 4 datos:", linea)
