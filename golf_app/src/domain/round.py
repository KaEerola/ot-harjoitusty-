class Round:
    """Represents a single golf round played by a user.

    A Round contains information about the course played,
    the score achieved, the date of the round, and the user
    who played it.
    """

    def __init__(self, round_id, course, score, date, user_id):
        """Initializes a new Round instance.

        Args:
            round_id (int): Unique identifier for the round.
            course (str): Name of the golf course.
            score (int): Player's score for the round.
            date (str): Date when the round was played (e.g. "YYYY-MM-DD").
            user_id (int): Identifier of the user who played the round.
        """
        self.id = round_id
        self.course = course
        self.score = score
        self.date = date
        self.user_id = user_id
