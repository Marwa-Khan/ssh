from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("Error",spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","'Apple'")
        self.assertEqual("Apple",spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","'Apple")
        self.assertEqual("#Error",spreadsheet.evaluate("A1"))

    def test_valid_formulas_string(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple",spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_integer(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","=5")
        self.assertEqual(5,spreadsheet.evaluate("A1"))

    def test_formula_evaluate_invalid_string(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","='Apple")
        self.assertEqual("#Error",spreadsheet.evaluate("A1"))


    def test_formula_refernces_valid(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1" ,"42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))


    def test_formula_references_invalid(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1","42.5")
        self.assertEqual("#Error",spreadsheet.evaluate("A1"))

    def test_formula_references_Circular(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1","=A1")
        self.assertEqual("#Circular",spreadsheet.evaluate("A1"))

    def test_formula_arithmetic_valid(self):
        spreadsheet=SpreadSheet()
        spreadsheet.set("A1","=1+3")
        self.assertEqual(4,spreadsheet.evaluate("A1"))

    def test_formula_arithmetic_error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_arithmetic_divideByZero_error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1/0")
        self.assertEqual("#Error",spreadsheet.evaluate("A1"))

    def test_formula_arithmetic_intValid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3*2")
        self.assertEqual(9, spreadsheet.evaluate("A1"))









