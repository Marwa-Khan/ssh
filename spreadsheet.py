
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluation_stack = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        if cell in self._evaluation_stack:
            return "#Circular"
        self._evaluation_stack.add(cell)
        
        value = self._cells.get(cell, "")
        if value.startswith("'"):
            if value.endswith("'"):
                result = value[1:-1]
            else:
                result = "#Error"
        elif value.startswith("="):
            if value[1:].startswith("'") and value[1:].endswith("'"):
                result = value[2:-1]
            elif value[1:].isnumeric():
                result = int(value[1:])
            elif value[1:] in self._cells:
                referenced_value = self.evaluate(value[1:])
                if isinstance(referenced_value, int):
                    result = referenced_value
                else:
                    result = "#Error"
            else:
                try:
                    # Evaluate the arithmetic expression safely
                    result = eval(value[1:], {"__builtins__": None}, {})
                    if not isinstance(result, int):
                        raise ValueError
                except:
                    result = "#Error"
        else:
            try:
                result = int(value)
            except ValueError:
                result = "Error"
        
        self._evaluation_stack.remove(cell)
        return result

