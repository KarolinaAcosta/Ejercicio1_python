from datetime import datetime

#Funcion para validar los campos de cada línea del archivo 
def check_fields(linea, numero_linea=None): 
    fields = linea.strip().split(",") 

# función para imprimir el mensaje de error
    def invalid(message): 
        if numero_linea is not None: # si se proporciona el número de línea
            print(f"La línea {numero_linea} no cumple: {message}: {linea.strip()}")  # imprime el mensaje de error con el número de línea y la línea completa
        return False, None # retorna False y None para indicar que la línea no es válida

    if len(fields) != 4: # si la línea no tiene exactamente 4 campos, retorna un mensaje de error
        return invalid("debe tener exactamente 4 campos")

# Validación de cada campo
    fecha, bot, ejecucion, tiempo = fields

# Validación de la fecha
    try:
        datetime.strptime(fecha, "%Y-%m-%d") # valida que la fecha tenga el formato AAAA-MM-DD
    except ValueError:
        return invalid("la fecha debe tener el formato AAAA-MM-DD")
    
# Validación del bot
    if (bot != "bot_facturas" and bot != "bot_nomina"
            and bot != "bot_cartera"):
        return invalid("el bot debe ser bot_facturas, bot_nomina o bot_cartera")

# Validación de la ejecución
    if ejecucion != "exitosa" and ejecucion != "fallida":
        return invalid("la ejecución debe ser exitosa o fallida")

#validación del tiempo
    if not tiempo.isdigit():
        return invalid("el tiempo debe ser un número entero")

#validación exitosa, retorna True y los campos validados
    if numero_linea is not None:
        print(f"La línea {numero_linea} cumple con los 4 campos: {linea.strip()}")
    return True, (fecha, bot, ejecucion, tiempo)
