from errors.validation_error import TypeValidationError
from errors.validation_error import RequiredFieldError
from errors.validation_error import RangeError
# Validators to verify that 
# - Value needs to be String
# - Value cannot be ""

def require_non_empty_str(field:str, value):
    # - Value needs to be String
    if not isinstance(value,str):
        raise TypeValidationError(field," must be a string") #Type validation error
    # - Value cannot be ""
    if not value.strip():
        raise RequiredFieldError(field," must not be empty") #Required validation error
    return value.strip()

# Validator to verify that
# - needs to be an integer
# - needs to be between min and max
def require_int_in_range(field: str, value, min_value: int, max_value: int):
    # Value needs to be an integer
    if not isinstance(value, int):
        raise TypeValidationError(field, "must be an integer")
    # Value needs to be between min and max
    if not (min_value <= value <= max_value):
        raise RangeError(field, f"must be between {min_value} and {max_value}")
    return value


def require_score_list(field: str, value):
    #Value needs to be a list
    if not isinstance(value, list):
        raise TypeValidationError(field, "must be a list of integers (0–100)")
    # for each item (s) in the list and the index (i)
    # [70, 50, 30, 80]
    # s -represents , 70, 50 ..
    # i -represnts 0,1,2,3
    for i, s in enumerate(value):
        # The item needs to be a number
        if not isinstance(s, int):
            raise TypeValidationError(field, f"score at index {i} must be an integer")
        # The item needs to be between 0 and 100
        if not (0 <= s <= 100):
            raise RangeError(field, f"score at index {i} must be between 0 and 100")
    return value

# Student Validator
# Validae dictionary so that it follows the proper validation rules
def validate_student_record(data: dict) -> dict:
    """
    Validate and normalize a student record.

    Expected keys:
        - name (str, non-empty)
        - age (int, 5–18)
        - scores (list[int], each 0–100)
    """
    if not isinstance(data, dict):
        raise TypeValidationError("data", "must be a dictionary")

    # Validate each field
    name = require_non_empty_str("name", data.get("name")) 
    # Name needs to be str and cannot be empty
    age = require_int_in_range("age", data.get("age"), 5, 18) 
    # Age needs be integer and between 5 and 8
    scores = require_score_list("scores", data.get("scores", [])) 
    # scores, needs to follow the rules
    # needs to be a list, only have number, all numbers between 0 and 100

    # Return normalized record
    #If everything is ok then only create it
    return {"name": name, "age": age, "scores": scores}
