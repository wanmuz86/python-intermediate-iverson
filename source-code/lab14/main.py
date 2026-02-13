import logging
from datetime import datetime
from utils.validator import compute_average, parse_numbers_from_text, compute_stats
from errors.error import AppError

LOG_FILE = "app_errors.log"

# retrieve the built-in / std logging module
# Set it up, it will be logged inside app_errors.log
# logging.INFO (level of log that will be logged in file)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="$(asctime)s | %(levelname)s | %(message)s"
)

print("=== Lab : Multi-Layer Exceptions + File Logging ===")
print(f"Logging errors to: {LOG_FILE}")

def run_average_workflow(user_text: str):
    """
    Main layer: orchestrates data + service layers.
    Logs errors to a file.
    """
    try:
        numbers = parse_numbers_from_text(user_text) # "1,2,3" => [1,2,3]
        avg = compute_average(numbers) # [1,2,3] => 2
        stats = compute_stats(numbers)
    except AppError as e:
        # Log full error including traceback
        logging.exception(f"Workflow failed for input: {user_text!r}")
         #Log an error , it will be logged in the file

        # Provide a friendly message
        print("Something went wrong. Please check your input.")
        print("Error type:", type(e).__name__)
        print("Message:", e)

        # Show root cause (from chaining)
        # the issue, retrieved from the Exception / Type of Exception

        if e.__cause__:
            print("Root cause:", repr(e.__cause__))
    else:
        print("Numbers:", numbers)
        print("Average:", avg)
        print(f"Min: {stats['min']}, Max: {stats['max']}, Median: {stats['median']}")
    finally:
        print("Workflow finished.\n")

def main():
    print("\n--- Case 1: Good input ---")
    run_average_workflow("10,20,30") # all OK
    run_average_workflow("5,1,2,4,7") # another positive example with non-sorted data

    print("\n--- Case 2: Bad parse (non-number) ---")
    run_average_workflow("10,xx,30") # DataError

    print("\n--- Case 3: Empty numbers (business rule fail) ---")
    run_average_workflow("") # ValuError -> number cannot be less than 0

    print("\nOpen the log file to view details:")
    print(LOG_FILE)

if __name__ == "__main__":
    main()
