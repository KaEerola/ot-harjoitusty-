class RoundService:
    """Provides application-level operations for managing golf rounds.

    This service acts as a layer between the UI and the repository,
    handling user-specific logic such as ensuring that actions are
    performed only on the currently logged-in user's data.
    """

    def __init__(self, auth_service, round_repo):
        """Initializes the round service.

        Args:
            auth_service (AuthService): Service providing the current user.
            round_repo (RoundRepository): Repository for round persistence.
        """
        self.auth = auth_service
        self.repo = round_repo

    def add_round(self, course, score, date):
        """Adds a new round for the current user.

        Args:
            course (str): Name of the golf course.
            score (int): Player's score.
            date (str): Date of the round (format: "YYYY-MM-DD").
        """
        user = self.auth.current_user
        self.repo.create(course, score, date, user["id"])

    def get_rounds(self):
        """Retrieves all rounds for the current user.

        Returns:
            list[Round]: List of the user's rounds.
        """
        user = self.auth.current_user
        return self.repo.get_by_user(user["id"])

    def delete_round(self, round_id):
        """Deletes a round belonging to the current user.

        Args:
            round_id (int): ID of the round to delete.

        Raises:
            PermissionError: If the round does not belong to the user
                or does not exist.
        """
        user = self.auth.current_user
        deleted = self.repo.delete(round_id, user["id"])

        if deleted == 0:
            raise PermissionError("Et voi poistaa tätä kierrosta")

    def update_round(self, round_id, course, score, date):
        """Updates a round belonging to the current user.

        Args:
            round_id (int): ID of the round to update.
            course (str): Updated course name.
            score (int): Updated score.
            date (str): Updated date (format: "YYYY-MM-DD").
        """
        user = self.auth.current_user
        self.repo.update(round_id, course, score, date, user["id"])
