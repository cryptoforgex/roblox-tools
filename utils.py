from typing import List, Dict, Any


def calculate_average(scores: List[float]) -> float:
    """Calculate the average of a list of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_high_scores(scores: List[float], threshold: float) -> List[float]:
    """Filter scores that are above a given threshold."""
    return [score for score in scores if score > threshold]


def format_scoreboard(scoreboard: Dict[str, float]) -> str:
    """Format a scoreboard dictionary into a string."""
    formatted = [f'{name}: {score:.2f}' for name, score in scoreboard.items()]
    return '\n'.join(formatted)


def is_valid_score(score: Any) -> bool:
    """Check if a score is a valid float."""
    return isinstance(score, (int, float)) and 0 <= score <= 100
