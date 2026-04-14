from src.domain.round import Round

class RoundService:
    def __init__(self):
        self._rounds = []

    def add_round(self, course, score, date):
        new_round = Round(course, score, date)
        self._rounds.append(new_round)

    def get_rounds(self):
        return self._rounds
