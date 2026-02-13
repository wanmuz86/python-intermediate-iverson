from errors.student_record_build_error import build_student_record
from errors.student_record_build_error import StudentRecordBuildError

print("=== Lab: Validation System + Custom Exception Hierarchy ===")

def test_cases():
    print("\n--- Test Cases ---")

    good = {"name": "Aina", "age": 7, "scores": [80, 90, 85]}
    bad_name = {"name": "", "age": 7, "scores": [80]} # Name should not be ""
    bad_age = {"name": "Ali", "age": 3, "scores": [70]} # Age shoild be between 5-18
    bad_scores = {"name": "Mira", "age": 8, "scores": [95, 150]} # score should be between 0 and 100
    
    #Add scenario where you put string inside score
    bad_scores_format = {"name":"Wan", "age":15, "scores":[70,"def"]} 

    # tuple ()
    cases = [("GOOD", good), ("BAD_NAME", bad_name), ("BAD_AGE", bad_age), 
             ("BAD_SCORES", bad_scores), ("BAD_SCORE_FORMAT",bad_scores_format)]

    # label is the left part "GOOD", "BAD_NAME"
    # data is the right part / test data 
    for label, data in cases:
        print(f"\nCase: {label}")
        try:
            record = build_student_record(data)
        except StudentRecordBuildError as e:
            print("Build error:", e)
            # show chained root cause
            print("Root cause:", repr(e.__cause__))
        else:
            print("Validated record:", record)
        finally:
            print("Done case:", label)

def main():
    test_cases()

if __name__ == "__main__":
    main()


