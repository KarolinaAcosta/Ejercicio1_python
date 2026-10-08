from validaciones import check_fields


def leer_ejecuciones():
    with open("ejecuciones.txt", "r", encoding="utf-8") as ejecuciones:
        lineas = ejecuciones.read().splitlines()
        for numero_linea, linea in enumerate(lineas, start=1):
            check_fields(linea, numero_linea)
