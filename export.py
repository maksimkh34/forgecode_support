# Глобальные переменные и флаги для запуска

# GLOBAL

class GlobalVariables:
    file_logging = True
    disable_file_exception = False
# GLOBAL


def boot_options(options: str):
    flags = options.split(" ")
    for flag in flags:
        match flag:
            case "-nofilelog":
                GlobalVariables.file_logging = False
            case "-disablefileexception":
                GlobalVariables.disable_file_exception = True
            case "-test":
                flags.append("-nofilelog")
                flags.append("-disablefileexception")
