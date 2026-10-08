#Funcion para crear el reporte de ejecuciones de los bots

def create_report(bots, lowest_bot, highest_bot):

    report = ""

    report += "REPORTE DE EJECUCIONES\n"
    report += "======================\n\n"

    for bot, indicators in bots.items():
        report += f"BOT: {bot}\n"
        report += f"Total de ejecuciones: {indicators['total']}\n"
        report += f"Ejecuciones exitosas: {indicators['successful']}\n"
        report += f"Ejecuciones fallidas: {indicators['failed']}\n"
        report += (
            f"Porcentaje de éxito: "
            f"{indicators['success_percentage']:.2f}%\n"
        )
        report += (
            f"Duración promedio: {indicators['average_time']:.2f}\n"
        )
        report += f"Duración máxima: {indicators['maximum_time']}\n"
        report += f"Duración mínima: {indicators['minimum_time']}\n\n"

        report += "COMPARACIÓN\n"
        report += "===========\n\n"
        report += f"Bot con menor porcentaje de éxito: {lowest_bot}\n"
        report += f"Bot con mayor duración promedio: {highest_bot}\n"

    with open("reporte.txt", "w", encoding="utf-8") as file:
         file.write(report)

         print(report) # Imprime el reporte en la consola