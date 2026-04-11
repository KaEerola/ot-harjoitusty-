from src.domain.round import Round

class RoundService:
    def __init__(self):
        self._rounds = []

    def add_round(self, course, score):
        new_round = Round(course, score)
        self._rounds.append(new_round)

    def get_rounds(self):
        return self._rounds