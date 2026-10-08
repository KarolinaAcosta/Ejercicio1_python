def create_report(bots, lowest_bot, highest_bot):
    with open("reporte.txt", "w", encoding="utf-8") as file:
        file.write("REPORTE DE EJECUCIONES\n")
        file.write("======================\n\n")

        for bot, indicators in bots.items():
            file.write(f"BOT: {bot}\n")
            file.write(f"Total de ejecuciones: {indicators['total']}\n")
            file.write(f"Ejecuciones exitosas: {indicators['successful']}\n")
            file.write(f"Ejecuciones fallidas: {indicators['failed']}\n")
            file.write(
                f"Porcentaje de éxito: "
                f"{indicators['success_percentage']:.2f}%\n"
            )
            file.write(
                f"Duración promedio: {indicators['average_time']:.2f}\n"
            )
            file.write(f"Duración máxima: {indicators['maximum_time']}\n")
            file.write(f"Duración mínima: {indicators['minimum_time']}\n\n")

        file.write("COMPARACIÓN\n")
        file.write("===========\n\n")
        file.write(f"Bot con menor porcentaje de éxito: {lowest_bot}\n")
        file.write(f"Bot con mayor duración promedio: {highest_bot}\n")