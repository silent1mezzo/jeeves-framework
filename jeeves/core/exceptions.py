class JeevesException(Exception):
    pass

class NotImplemented(JeevesException, NotImplementedError):
    pass

class InvalidCommand(JeevesException):
    pass

class ImproperlyConfigured(JeevesException):
    pass

class InvalidPlugin(JeevesException):
    pass
