from pathlib import Path

from app.utils import SCORES_FILE_NAME


def add_score(difficulty: int) -> None:
    scores_file_path = Path(SCORES_FILE_NAME)
    current_score = int(Path(SCORES_FILE_NAME).read_text()) if scores_file_path.exists() else 0
    new_score = current_score + (difficulty*3) + 5
    scores_file_path.write_text(str(new_score))
