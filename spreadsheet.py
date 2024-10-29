
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: int) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str) -> int:
        return int(self._cells[cell])

