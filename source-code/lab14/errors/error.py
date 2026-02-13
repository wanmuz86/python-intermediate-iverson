class AppError(Exception):
    """Base class for app-level exceptions."""
    pass


class DataError(AppError):
    """Raised when data access/parsing fails."""
    pass


class ServiceError(AppError):
    """Raised when business logic fails."""
    pass


class UserInputError(AppError):
    """Raised when user input is invalid."""
    pass
