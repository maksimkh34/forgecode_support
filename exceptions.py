# Локальные исключения

class InvalidLoginFileException(Exception):
    """Log file with provided index isn't in database"""
    pass


class FileLoggingRestricted(Exception):
    """File logging is restricted (by flag or something else)"""
    pass
