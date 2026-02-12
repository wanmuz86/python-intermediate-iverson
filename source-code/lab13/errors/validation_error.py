from .app_error import AppError

# All validation error will be based on this Class
# In production (will be demonstrated in lab 14)
# You might baseclass for different type of error
# ServiceError, DatabaseError, LogicError .....
#  
class ValidationError(AppError):

    def __init__(self, field:str, message:str):
        super().__init__(f"{field}:{message}")
        self.field = field
        self.message = message

class RequiredFieldError(ValidationError):
    """Raised when a required field is missing or empty."""
    pass


class RangeError(ValidationError):
    """Raised when a numeric value is out of range."""
    pass


class TypeValidationError(ValidationError):
    """Raised when a value has the wrong type."""
    pass
