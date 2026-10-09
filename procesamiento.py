from validaciones import check_fields

# función para procesar el archivo y separar las ejecuciones exitosas, fallidas e inválidas
def process_file(file_name): 
    successful = []
    failed = []
    invalid = []

#Diccionarios para contar las lineas invalidas segun motivo

    invalid_reasons = {
        "linea vacia": 0,
        "debe tener exactamente 4 campos": 0,
        "la fecha debe tener el formato AAAA-MM-DD": 0,
        "el bot debe ser bot_facturas, bot_nomina o bot_cartera": 0,
        "la ejecución debe ser exitosa o fallida": 0,
        "el tiempo debe ser un número entero": 0
    }

    try:

        with open(file_name, "r", encoding="utf-8") as file: # encoding outf-8  para aceptar caracteres especiales
            for number_lines, line in enumerate(file, start=1): 
                valid, result, reason = check_fields(line, number_lines) # validación de los campos de cada línea del archivo

                if not valid:
                    invalid.append(line.strip())
                    if reason in invalid_reasons:
                        invalid_reasons[reason] += 1
                    continue

                date, bot, execution, time = result # datos validados de la línea
                time = int(time) # Pide el tiempo de ejecución como un entero
                execution_data = (date, bot, execution, time) # execution_data es una tupla que contiene los datos de la ejecución

                if execution == "exitosa":
                    successful.append(execution_data) # agrega la ejecución exitosa a la lista de ejecuciones exitosas
                else:
                    failed.append(execution_data) # agrega la ejecución fallida a la lista de ejecuciones fallidas

    except FileNotFoundError:
        print(f"El archivo {file_name} no se encontró.")
    return successful, failed, invalid, invalid_reasons # retorna las ejecuciones exitosas, fallidas e inválidas como listas de tuplas

    