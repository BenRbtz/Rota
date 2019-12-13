from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Instructor:
    name: str
    preferred_days: List[str]
    teach: Optional[int] = None
