from typing import Tuple


class RawDataModel:
    location: Tuple[float, float]
    label: str

    def __init__(self, x: float, y: float, label: str):
        self.location = (x, y)
        self.label = label
