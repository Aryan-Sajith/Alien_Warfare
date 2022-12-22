class FileIO:
    """A class to manage input/output of game data files.
    """

    def __init__(self, dir):
        """Initializes the FileIO handler.
        :param str dir: specifies what type of FileIO to perform.
        """
        self.dir = dir

    def input_high_score(self) -> int:
        """Input high score from output/high_score.txt if it exists"""
        try:  # File exists
            with open(self.dir, 'r') as f:
                return int(float(f.read()))
        except FileNotFoundError:  # Default value
            return 0

    def output_gamedata(self, high_score):
        """Outputs game data to a file for later usage."""
        # High score storage
        self._store_alltime_highscore(high_score)

    def _store_alltime_highscore(self, high_score):
        """Manages FileIO for all-time high score."""
        # Create high_score.txt
        self._create_highscore_document(high_score, self.dir)
        # Update high_score.txt
        self._update_highscore_document(high_score, self.dir)

    def _create_highscore_document(self, high_score, high_score_dir):
        """Initially creates the output/high_score.txt file with data"""
        with open(high_score_dir, 'w') as f:
            f.write(str(high_score))

    def _update_highscore_document(self, high_score, high_score_dir):
        """Updates the output/high_score.txt file with data"""
        with open(high_score_dir, 'r') as f:
            file_high_score = int(float(f.read()))
        with open(high_score_dir, 'w') as f:
            overall_high_score_str = max(high_score, file_high_score)
            f.write(str(overall_high_score_str))
