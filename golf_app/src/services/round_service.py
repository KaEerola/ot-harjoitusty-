class RoundService:
    def __init__(self, auth_service, round_repo):
        self.auth = auth_service
        self.repo = round_repo

    def add_round(self, course, score, date):
        user = self.auth.current_user
        self.repo.create(course, score, date, user["id"])

    def get_rounds(self):
        user = self.auth.current_user
        return self.repo.get_by_user(user["id"])

    def delete_round(self, round_id):
        user = self.auth.current_user
        deleted = self.repo.delete(round_id, user["id"])

        if deleted == 0:
            raise PermissionError("Et voi poistaa tätä kierrosta")

    def update_round(self, round_id, course, score, date):
        user = self.auth.current_user
        self.repo.update(round_id, course, score, date, user["id"])