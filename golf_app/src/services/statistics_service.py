class StatisticsService:
    """Provides statistical calculations for a user's golf rounds.

    This service uses RoundRepository to fetch rounds and
    AuthService to determine the currently logged-in user.
    It supports filtering rounds by date and calculating
    various statistics such as averages and best scores.
    """
    def __init__(self, round_repository, auth_service):
        """Initializes the statistics service.

        Args:
            round_repository (RoundRepository): Repository for accessing round data.
            auth_service (AuthService): Service for handling authentication and current user.
        """
        self._repo = round_repository
        self._auth = auth_service

    def _get_user_rounds(self):
        """Fetches all rounds for the currently logged-in user.

        Returns:
            list[Round]: List of the user's rounds.
        """
        user = self._auth.current_user
        return self._repo.get_by_user(user["id"])

    def _filter_by_date(self, rounds, start_date, end_date):
        """Filters rounds by a date range.

        Args:
            rounds (list[Round]): List of rounds to filter.
            start_date (date | None): Start date (inclusive).
            end_date (date | None): End date (inclusive).

        Returns:
            list[Round]: Filtered list of rounds.
        """
        if not start_date and not end_date:
            return rounds

        filtered = []

        for r in rounds:
            if start_date and r.date < start_date:
                continue
            if end_date and r.date > end_date:
                continue
            filtered.append(r)

        return filtered

    def average_score(self, start_date=None, end_date=None):
        """Calculates the average score for the user.

        Args:
            start_date (date | None): Optional start date filter.
            end_date (date | None): Optional end date filter.

        Returns:
            float | None: Average score, or None if no rounds exist.
        """
        rounds = self._filter_by_date(self._get_user_rounds(), start_date, end_date)

        if not rounds:
            return None

        return sum(r.score for r in rounds) / len(rounds)

    def best_score(self, start_date=None, end_date=None):
        """Finds the best (lowest) score for the user.

        Args:
            start_date (date | None): Optional start date filter.
            end_date (date | None): Optional end date filter.

        Returns:
            int | None: Best score, or None if no rounds exist.
        """
        rounds = self._filter_by_date(self._get_user_rounds(), start_date, end_date)

        if not rounds:
            return None

        return min(r.score for r in rounds)

    def total_rounds(self, start_date=None, end_date=None):
        """Counts the total number of rounds.

        Args:
            start_date (date | None): Optional start date filter.
            end_date (date | None): Optional end date filter.

        Returns:
            int: Number of rounds.
        """
        rounds = self._filter_by_date(self._get_user_rounds(), start_date, end_date)
        return len(rounds)

    def last_n_rounds(self, n):
        """Returns the most recent N rounds.

        Args:
            n (int): Number of rounds to return.

        Returns:
            list[Round]: List of the most recent rounds.
        """
        rounds = sorted(
            self._get_user_rounds(),
            key=lambda r: r.date,
            reverse=True
        )
        return rounds[:n]

    def average_last_10_vs_all(self):
        """Compares the average of the last 10 rounds to all rounds.

        Returns:
            tuple[float | None, float | None]:
                A tuple (last_10_avg, all_avg).
                Returns (None, None) if no rounds exist.
        """
        all_rounds = self._get_user_rounds()

        if not all_rounds:
            return None, None

        all_avg = sum(r.score for r in all_rounds) / len(all_rounds)

        last_10 = sorted(all_rounds, key=lambda r: r.date, reverse=True)[:10]
        last_10_avg = sum(r.score for r in last_10) / len(last_10)

        return last_10_avg, all_avg
