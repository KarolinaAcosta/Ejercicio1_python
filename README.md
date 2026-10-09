# SISTEMA DE BOTS

## DESCRIPCION DEL SISTEMA

Este proyecto, se comprende de leer y validar la información en una base en archivo .txt, 
el programa busca identificar especialmente las líneas validas e incorrectas para generar
un reporte final.

## FUNCIONES

Contiene las siguientes funciones principales
1. Leer datos desde un archivo txt
2. Validar el formato de los datos, línea por linea
3. Agrupar datos por bot
4. Calcular una serie de indicadores por cada bot
5. Comparar datos de los bot segun los indicadores
6. Generar un reporte en formato txt

## QUE ARCHIVOS CONFORMAN EL PROYECTO

El proyecto cuenta con 7 archivos:
"principal.py": Es el encargado de ejecutar todas las funciones en un solo archivo o una unica linea
"lectura-py" : Se encarga de leer el archivo ejecuciones.txt
"validacion.py" Es el principal encargado de revisar linea por linea para asegurar el formato correspondiente
"procesamiento.py": Organiza y separa los datos
"indicadores.py": Calcula los indicadores de cada bot
"comparacion.py": Realiza la comparación de los resultados de los indicadores de los bots
"reporte.py": Se encarga de generar el reporte final con los resultados de los indicadores
"ejecuciones.txt": Con tiene la base de datos o líneas de entrada
"reporte.txt": Podreos visualizar el reporte final generado por el archivo reporte.py

## ¿COMO EJECUTARLO?

Debemos ejecutar el archivo:
principal.py
Este mismo procesara, ejecuciones.txt y generara un archivo llamado reporte.txt
