
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        value = self._cells[cell]
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        try:
            return int(value)
        except ValueError:
            return "Error"

