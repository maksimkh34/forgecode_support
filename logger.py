# Модуль с описанием логгера, который будет выводить (сохранять) действия и работу бота (как дебагер)

import enum
import datetime
from colorama import Fore

import export
from exceptions import InvalidLoginFileException, FileLoggingRestricted


class LogType(enum.Enum):  # Перечисление для логгера (для понимания смысла информации)

    ERR = 1  # Ошибка, работу продолжать нельзя
    OK = 2  # Задача выполнена успешно
    INF = 3  # Информирование о действиях пользователя (или чем-то еще)
    WARN = 4  # Предупреждение о возможной неработоспособности
    UNW = 5  # Некритичная ошибка (функция еще не доработана, и др)

    def to_string(self) -> str:
        match self.value:
            case 1:
                return "ERR"
            case 2:
                return "OK"
            case 3:
                return "INF"
            case 4:
                return "WARN"
            case 5:
                return "UNW"
        return "%ENUM_ERR%"

    def get_color(self):
        match self.value:
            case 1:
                return Fore.RED
            case 2:
                return Fore.GREEN
            case 3:
                return Fore.BLUE
            case 4:
                return Fore.YELLOW
            case 5:
                return Fore.CYAN
        return "%COLOR_ERR%"


class Logger:
    log_files = []

    def __init__(self, main_log_file_root=""):
        main_log_file_path = f"{main_log_file_root}forgecode.{datetime.datetime.now().year}." \
                             f"{datetime.datetime.now().month}.{datetime.datetime.now().day}_" \
                             f"{datetime.datetime.now().hour}.{datetime.datetime.now().minute}.log"

        if export.GlobalVariables.file_logging:
            self.log_files = [open(main_log_file_path, "w")]

    def log(self, text: str, log_type=LogType.INF,
            log_file_index=0, log_to_file=True):

        print_color = log_type.get_color()

        print(f"{log_type.to_string()}:\t{print_color}{datetime.datetime.now().hour}:"
              f"{datetime.datetime.now().minute}:\t{text}{Fore.RESET}")

        if not export.GlobalVariables.file_logging:
            return

        if log_file_index >= len(self.log_files):
            raise InvalidLoginFileException("Seems like there is no log file bound to provided index")

        if log_to_file:
            self.log_files[log_file_index]\
                .write(f"{datetime.datetime.now().day}."
                       f"{datetime.datetime.now().month}: "
                       f"{datetime.datetime.now().hour}.{datetime.datetime.now().minute}: "
                       f"{log_type.to_string()}:\t{text}\n")

    def add_log_file(self, log_file_path: str):
        if export.GlobalVariables.file_logging:
            self.log_files.append(open(log_file_path, "w"))
        elif not export.GlobalVariables.disable_file_exception:
            raise FileLoggingRestricted("Logging to file is restricted (probably, by -nofilelog flag)")
