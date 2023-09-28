# Локальные исключения

class InvalidLoginFileException(Exception):
    """Log file with provided key isn't in dictionary"""
    pass


class FileLoggingRestricted(Exception):
    """File logging is restricted (by flag or something else)"""
    pass
