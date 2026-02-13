from errors.error import DataError, ServiceError

# Data validation
def parse_numbers_from_text(text: str):
    """
    Data layer: parse comma-separated integers.
    Example input: "10,20,30"
    """
    try:
        # Split the text, based on delimiter and make it as a List

        # Transfrom string to List, based on given delimiter/separator
        # 10,20,30 -> delimiter is , => [10,20,30]
        parts = text.split(",")

        # strip => remove the whitespace
        return [int(p.strip()) for p in parts]
    
    except Exception as e:
        # Convert low-level parsing errors into a data-layer exception
        raise DataError("Failed to parse numbers from data source") from e


def compute_average(numbers):
    """
    Service layer: compute average of a list of numbers.
    Business rule: list must not be empty.
    """
    try:
        # numbers is not given 
        if not numbers:
            raise ValueError("No numbers provided")
        #sum(numbers) -> sum of all item in the list
        #len(numbers)-< how many item in the list
        # parse_numbers_from_text("")  => [] => len(numbers) => 0 -> raise exception 
        return sum(numbers) / len(numbers) 
    # calculate the average of the given list
    except Exception as e:
        raise ServiceError("Average calculation failed") from e
    
def compute_stats(numbers):
    if not numbers:
        raise ServiceError("Stats calculation failed") from ValueError("No numbers provided")

    # Sort the number   [5,1,4,2,6,7] => [1,2,4,5,6,7]
    # remember yesterday example reverse=True if you want it to be in reverse
    nums = sorted(numbers)
    # how many items are there  n = 5
    n = len(nums)
    # 5 / 2 (integer value) = 2
    mid = n // 2

    # n % 2 == 1 [odd] => 5 % 2 == 1 [True]
    # median nums[2] => 4
    median = float(nums[mid]) if n % 2 == 1 else (nums[mid - 1] + nums[mid]) / 2.0

    # min and max is built in Python function to get min and max from a list
    return {"min": min(nums), "max": max(nums), "median": median}
