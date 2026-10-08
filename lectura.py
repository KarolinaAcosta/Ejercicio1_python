from validaciones import check_fields


def read_lines():
    with open("ejecuciones.txt", "r", encoding="utf-8") as ejecuciones:
        lines = ejecuciones.read().splitlines() # Lee todas las líneas del archivo y las divide en una lista de líneas sin los saltos de línea
        validated_lines = []
        for numero_linea, linea in enumerate(lines, start=1): # Enumera las líneas comenzando desde 1
            es_valida = check_fields(linea, numero_linea) 
            validated_lines.append((linea, es_valida)) # append agrega a la lista validated_lines

        return validated_lines
