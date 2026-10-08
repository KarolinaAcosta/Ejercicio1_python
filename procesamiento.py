from validaciones import check_fields


def process_file(file_name):
    successful = []
    failed = []
    invalid = []

    with open(file_name, "r", encoding="utf-8") as file:
        for numero_linea, line in enumerate(file, start=1):
            valid, result = check_fields(line, numero_linea)

            if not valid:
                invalid.append(line.strip())
                continue

            date, bot, execution, time = result
            time = int(time)
            execution_data = (date, bot, execution, time)

            if execution == "exitosa":
                successful.append(execution_data)
            else:
                failed.append(execution_data)

    return successful, failed, invalid