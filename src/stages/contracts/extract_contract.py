from typing import NamedTuple
from datetime import date


class ExtractContract(NamedTuple):
    raw_information_content: list[dict[str, str]]
    extraction_date: date
