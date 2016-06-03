#!/usr/bin/env python
"""Example usage of terminaltables using colorclass.

Just prints sample text and exits.
"""

from colorclass import Color
from terminaltables import SingleTable

table_data = [
    [Color('Low Space'), Color('{autocyan}Nominal Space{/autocyan}'), Color('Excessive Space')],
    [Color('Low Load'), Color('Nominal Load'), Color('{autored}High Load{/autored}')],
    [Color('{autocyan}Low Free RAM{/autocyan}'), Color('Nominal Free RAM'), Color('High Free RAM')],
]
table = SingleTable(table_data)
#table.title = '192.168.0.105'
#table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
#table.inner_heading_row_border = True
#table.inner_row_border = False
#table.outer_border = True
print
print(table.table)

