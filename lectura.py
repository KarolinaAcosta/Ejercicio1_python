from validaciones import check_fields


def leer_ejecuciones():
    with open("ejecuciones.txt", "r", encoding="utf-8") as ejecuciones:
        lineas = ejecuciones.read().splitlines()
        lineas_validadas = []
        for numero_linea, linea in enumerate(lineas, start=1):
            es_valida = check_fields(linea, numero_linea)
            lineas_validadas.append((linea, es_valida))
        return lineas_validadas
