
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
            expr = value[1:]
            if expr.startswith("'") and expr.endswith("'"):
                result = expr[1:-1]
            elif expr.isnumeric():
                result = int(expr)
            elif expr in self._cells:
                referenced_value = self.evaluate(expr)
                if isinstance(referenced_value, int):
                    result = referenced_value
                else:
                    result = "#Error"
            else:
                try:
                    # Evaluate the arithmetic expression safely
                    result = eval(expr, {"__builtins__": None}, self._cells)
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

