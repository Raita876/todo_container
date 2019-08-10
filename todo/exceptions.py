class TodoError(Exception):
    pass


class ArgumentError(TodoError):
    def __init__(self, message=None):
        self.message = "Argument Error." if message is None else message


class DatabaseError(TodoError):
    def __init__(self, message=None):
        self.message = "Database Error." if message is None else message

