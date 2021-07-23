from flask_table import Table, Col
import pandas as pd
import utility_functions as uf


# Declare chess table class
class ChessTable(Table):
    name = Col('Name')
    description = Col('Description')
