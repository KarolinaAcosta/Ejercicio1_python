# Función para calcular los indicadores de cada bot

def calculate_indicators(successful, failed): # successful significa ejecuciones exitosas y failed significa ejecuciones fallidas
    bots = {} # diccionario para almacenar los indicadores de cada bot
    all_executions = successful + failed 

    for _, bot, execution, time in all_executions:
        if bot not in bots: # Si el bot no está en el diccionario, se inicializa con los indicadores en cero y una lista vacía para los tiempos de ejecución
            bots[bot] = { 
                "total": 0,
                "successful": 0,
                "failed": 0,
                "times": [],
            }

        bot_indicators = bots[bot]
        bot_indicators["total"] += 1 # +1 hace referencia a que se ha procesado una ejecución más para ese bot
        bot_indicators["times"].append(time) # append agrega el tiempo de ejecución a la lista de tiempos del bot

        if execution == "exitosa":
            bot_indicators["successful"] += 1
        else:
            bot_indicators["failed"] += 1

    for bot_indicators in bots.values(): # Recorre los indicadores de cada bot
        total = bot_indicators["total"] # Obtiene el total de ejecuciones para ese bot      
        times = bot_indicators["times"] # Obtiene la lista de tiempos de ejecución para ese bot

        bot_indicators["success_percentage"] = (
            bot_indicators["successful"] / total
        ) * 100
        bot_indicators["average_time"] = sum(times) / len(times) # Calcula el tiempo promedio de ejecución para ese bot
        bot_indicators["maximum_time"] = max(times) # Calcula el tiempo máximo de ejecución para ese bot
        bot_indicators["minimum_time"] = min(times) # Calcula el tiempo mínimo de ejecución para ese bot

    return bots #retorna el diccionario con los indicadores de cada bots