# Base class for all app related error
# Best practice: All the other error classes will inherit this class

class AppError(Exception):
    """Base class for all custom application errors"""
    pass