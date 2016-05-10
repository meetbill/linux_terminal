#!/usr/bin/env python
"""Simple example usage of terminaltables without any other dependencies.

Just prints sample text and exits.
"""

from __future__ import print_function

from colorclass import Color, Windows
from terminaltables import AsciiTable, DoubleTable


table_data = [
    [Color('ID'), 'Years', 'Mysql_M'],
    [Color('1'), '2007-2009', Color('{autobggreen}YES{/bggreen}')],
    [Color('2'), '2009-2013', Color('{autobggreen}YES{/bggreen}')],
]
table = AsciiTable(table_data, 'wangbin')
print()
print(table.table)
