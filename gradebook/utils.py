def parse_grade(value):
    """
    Converts input to a float and validates it if is between 0 and 100.
    Raises ValueError with a specific message if validation fails.
    """
    try:
        grade = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid Input: '{value}' is not a valid number.")
    
    if not (0 <= grade <= 100):
        raise ValueError(f"Grade {grade} should be between 0 and 100.")
    
    return grade