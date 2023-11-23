from typing import Dict
from Options import Choice, Option, DeathLink, Range


class ScoreRequiredHundreds(Range):
    """The high score required to win divided by 100."""
    display_name = "Required Score (hundreds)"
    default = 50
    range_start = 1
    range_end = 100






ucn_options: Dict[str, type(Option)] = {
    "score_required":  ScoreRequiredHundreds,
    "Death Link": DeathLink

}
