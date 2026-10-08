#Funcion para comparar los bots y devolver el bot con menor porcentaje de éxito y el bot con mayor duración promedio

def compare_bots(bots):
    if not bots:
        return None, None

    lowest_bot = None # lowest_bot es el bot con menor porcentaje de éxito
    lowest_percentage = None # lowest_percentage es el porcentaje de éxito del bot con menor porcentaje de éxito
    highest_bot = None # highest_bot es el bot con mayor duración promedio
    highest_average = None # highest_average es la duración promedio del bot con mayor duración promedio

    for bot, indicators in bots.items(): # Recorre los bots y sus indicadores
        percentage = indicators["success_percentage"] 
        average = indicators["average_time"]

        if lowest_percentage is None or percentage < lowest_percentage: # compara el porcentaje de éxito del bot actual con el menor porcentaje de éxito encontrado hasta ahora
            lowest_percentage = percentage # actualiza el menor porcentaje de éxito encontrado
            lowest_bot = bot # actualiza el bot con menor porcentaje de éxito encontrado 

        if highest_average is None or average > highest_average: # compara la duración promedio del bot actual con la mayor duración promedio encontrada hasta ahora
            highest_average = average # actualiza la mayor duración promedio encontrada
            highest_bot = bot # actualiza el bot con mayor duración promedio encontrado
 
    return lowest_bot, highest_bot  # Retorna el bot con menor porcentaje de éxito y el bot con mayor duración promedio