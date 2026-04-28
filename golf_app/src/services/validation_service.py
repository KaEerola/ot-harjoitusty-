from datetime import date, datetime

def validate_inputs(course, score_input, date_input):
    """Validates the input values for a new round.

    Args:
        course (str): The golf course name.
        score_input (int): The score for the round.
        date_input (datetime.date): The date of the round.

    Raises:
        ValueError: If any of the input values are invalid.
        ValueError: If the course name is empty.
        ValueError: If the score is not a positive integer.
        ValueError: If the date is not in the correct format.

    Returns:
        tuple: A tuple containing the validated course name, score, and date.
    """
    if not course:
        raise ValueError("Course ei voi olla tyhjä")

    try:
        score = int(score_input)
    except ValueError as exc:
        raise ValueError("Score täytyy olla kokonaisluku") from exc

    if score <= 0:
        raise ValueError("Score täytyy olla positiivinen")

    if not date_input:
        date_input = date.today().isoformat()
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Päivämäärän muoto: YYYY-MM-DD") from exc

    return course, score, date_input
