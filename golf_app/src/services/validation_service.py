from datetime import date, datetime

def validate_inputs(course, score_input, date_input):
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
