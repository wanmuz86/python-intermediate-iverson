from errors.validation_error import ValidationError
from errors.app_error import AppError
from utils.validators import validate_student_record

class StudentRecordBuildError(AppError):
    """Raised when building a StudentRecord fails."""
    pass


def build_student_record(data: dict) -> dict:
    """
    Higher-level builder that adds context while preserving original errors.
    """
    try:
        # Validate the student then only create it
        return validate_student_record(data)
    # Throw a StudentRecordBuildError
    except ValidationError as e:
        # Add context but keep original error
        raise StudentRecordBuildError("Failed to build student record") from e
