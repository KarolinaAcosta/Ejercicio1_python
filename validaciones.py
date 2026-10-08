from datetime import datetime


def check_fields(linea, numero_linea=None):
    fields = linea.strip().split(",")

    def invalid(message):
        if numero_linea is not None:
            print(f"La línea {numero_linea} no cumple: {message}: {linea.strip()}")
        return False, None

    if len(fields) != 4:
        return invalid("debe tener exactamente 4 campos")

    fecha, bot, ejecucion, tiempo = fields

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return invalid("la fecha debe tener el formato AAAA-MM-DD")

    if (bot != "bot_facturas" and bot != "bot_nomina"
            and bot != "bot_cartera"):
        return invalid("el bot debe ser bot_facturas, bot_nomina o bot_cartera")

    if ejecucion != "exitosa" and ejecucion != "fallida":
        return invalid("la ejecución debe ser exitosa o fallida")

    if not tiempo.isdigit():
        return invalid("el tiempo debe ser un número entero")

    if numero_linea is not None:
        print(f"La línea {numero_linea} cumple con los 4 campos: {linea.strip()}")
    return True, (fecha, bot, ejecucion, tiempo)
