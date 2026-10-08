#importamos las funciones de los otros archivos

from lectura import read_lines
from procesamiento import process_file
from indicadores import calculate_indicators
from comparacion import compare_bots
from reporte import create_report

# Procesamos las ejecuciones exitosas, fallidas e inválidas
successful, failed, invalid = process_file("ejecuciones.txt")

# Calculamos los indicadores de cada bot
bots = calculate_indicators(successful, failed)

# Comparamos los bots y obtenemos el bot con menor porcentaje de éxito y el bot con mayor duración promedio
lowest_bot, highest_bot = compare_bots(bots)

#creaaos el reporte con los indicadores de cada bot
create_report(bots, lowest_bot, highest_bot)

print("Reporte creado correctamente.")

