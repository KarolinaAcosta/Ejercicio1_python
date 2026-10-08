from validaciones import check_fields


def read_lines():

    try:
        with open("ejecuciones.txt", "r", encoding="utf-8") as ejecuciones:
            lines = ejecuciones.read().splitlines() # Lee todas las líneas del archivo y las divide en una lista de líneas sin los saltos de línea
            return lines
    except FileNotFoundError:   
        print("El archivo ejecuciones.txt no se encontró.") 


        return []
