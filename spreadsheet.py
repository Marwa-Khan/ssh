
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        value = self._cells.get(cell, "")
        if value.startswith("'"):
            if value.endswith("'"):
                return value[1:-1]
            else:
                return "#Error"
        elif value.startswith("="):
            if value[1:].startswith("'") and value[1:].endswith("'"):
                return value[2:-1]
            try:
                return int(value[1:])
            except ValueError:
                return "#Error"
        else:
            try:
                return int(value)
            except ValueError:
                return "Error"

