from dataclasses import dataclass
from typing import Literal


@dataclass
class Criteria:
    is_amateur: bool
    target_rating_category: Literal["LOW", "MEDIUM", "HIGH"]
    target_genres: list[str]
