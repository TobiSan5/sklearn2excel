from pathlib import Path
from typing import List, TextIO, DefaultDict

from sklearn.tree import BaseDecisionTree
from sklearn.tree import export_text

import xlsxwriter

from .core import DecisionTreeTable

def export_decisiontrees_to_file(dt_list: List[BaseDecisionTree],
                                full_path: Path,
                                features: List[str]) -> None:
    """Documentation here."""
    # look for the greatest dept in BaseDecisionTree.estimators_
    depth = 0
    for dt in dt_list:
        if (dpt := dt.get_depth()) > depth:
            print(dpt)
            depth = dpt
    if depth == 0:
        raise ValueError("Seems like :param: dt_list has no valid decision tree.")
    all_text = []
    for dt in dt_list:
        all_text.append(export_text(decision_tree=dt, feature_names=features, max_depth=depth))
    with open(full_path, "w") as f:
        for text in all_text:
            f.write(text)


def parse_file_to_list(filepath: str) -> List[List[str]]:
    """Documentation here."""
    result = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            result.append(line.split())
    return result

def create_xlfile(decision_tree_table: DecisionTreeTable,
                  file_path: str = 'output.xlsx') -> None:
    """Writes an DecisionTreeTable object to an Excel file."""
    assert type(decision_tree_table) is DecisionTreeTable
    assert file_path.split('.')[-1] == 'xlsx', "File path must end with .xlsx"

    def rc2a1(row: int, col: int) -> str:
        """A1 notation from zero-indexed row-column indexes."""
        assert 0 <= row <= 1048575, "Row index out-of bounds."
        assert 0 <= col <= 16383, "Column index out-of bounds."

        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s_col = ''
        s_row = str(row + 1)
        b = col // 26 - 1
        a = col % 26
        if b >= 0:
            if b > 25:
                c = b // 26 - 1
                s_col += alph[c]
                b = b - (c + 1) * 26
            s_col += alph[b]
        s_col += alph[a]
        return s_col + s_row

    n_rows = decision_tree_table.n_rows
    n_tests = decision_tree_table.n_tests
    tests_col_pos = 2
    tests_row_pos = 0
    _dtt = decision_tree_table

    # create Excel object and two worksheets
    xl = xlsxwriter.Workbook(file_path)
    sheet_front = xl.add_worksheet(name='Front')
    sheet_table = xl.add_worksheet(name='DTTable')

    # write DecisionTreeTable tests and results into sheet DTTable
    for i_row in range(1, n_rows + 1):
        row_pos = tests_row_pos + i_row - 1
        for j_test in range(1, n_tests + 1):
            col_pos = tests_col_pos + j_test - 1
            sheet_table.write_formula(row_pos, col_pos, _dtt.get_test(i_row, j_test, as_formula=True))
        sheet_table.write_formula(
            row_pos,
            tests_col_pos - 1,
            f'=AND({rc2a1(row_pos, tests_col_pos)}:'+\
                f'{rc2a1(row_pos, tests_col_pos + n_tests - 1)})'
        )
        rc_ref_all_test = rc2a1(row_pos, tests_col_pos - 1)
        sheet_table.write_formula(
            row_pos,
            tests_col_pos - 2,
            f'=IF({rc_ref_all_test},{_dtt.get_result(i_row)},"")'
        )
    xl.close()