from typing import Callable, List, Union, Set, Tuple, Any


class DecisionTreeTable:
    """An table-like object created from a parsed collection of sklearn decision trees,
    which has first been exported as text to a file, and then transformed to
    a list of lines consisting of discrete elements."""
    source: List[List]
    _rows: dict[Any, Any]
    _width: int
    _features: Set[str]

    def __init__(self, source: List[List] = [[], ]):
        """    :source -- decision tree lines of elements"""
        # setup attributes
        # store source as attribute (for abundancy, not used)
        self.source = source
        # setup row dict attribute
        self._rows = {}
        # setup hidden width attribute
        # accessed by n_tests property
        self._width = 0
        # setup hidden features attribute
        # filled-in by parse_source() method
        # accessed by get_features() method
        self._features = set()

        # parse the source if not empty
        if len(source[0]) > 0:
            self.parse_source(source)

        # finally, in init
        pass

    def parse_source(self, source: List[List]):
        # setup counter for maximum column width
        column_count: int = 0
        # setup counter for tree
        tree_count: int = 0
        # setup counter and first row-item for rows
        row_count: int = 1
        self._rows[1] = {'tests': {}, 'result': None, 'tree': 1}
        # setup of lambda functions to interpret line
        # lambda to return columns in line
        ccount_f: Callable = lambda l: sum([1 if e[0] == '|' else 0 for e in l])
        # lambda to return result, if present, else None
        result_f: Callable = \
            lambda l: float(l[-1].strip('[]')) if l[-2] in ['value:', 'class:'] else None
        # lambda to return test, if present, else None
        test_f: Callable = lambda l: (l[-3], l[-2], float(l[-1])) \
            if l[-2] in ['<=', '>=', '<', '>', '=='] \
            else None

        # iteration through source lines
        # each line should consist of a list of strings
        # each line should contain one or more column indicators ('|')
        line: list
        for line in source:
            # get the column indicator
            x: int = ccount_f(line)
            # get the result or None
            result: Union[float, None] = result_f(line)
            # get the test or None
            test: Union[Tuple[str, str, float], None] = test_f(line)
            # check the column indicator
            # if it exceeds column max count, update column max count
            # if it is 1, update tree count
            # and setup test buffer for last seen tests
            if x > column_count:
                column_count = x
            if x == 1:
                tree_count += 1
                test_buffer: dict[int, dict[str, Union[str, float]]] = {}
            # check if line contains a result
            # if so, update result in row dict
            # and start a new row and initialise a row dict
            if result is not None:
                self._rows[row_count]['result'] = result
                row_count += 1
                self._rows[row_count] = {'tests': {}, 'result': None, 'tree': tree_count}
            # check if line contains a test
            # if so, update tests in row dict
            # and add test to test buffer
            if test is not None:
                self._features.add(test[0])
                self._rows[row_count]['tests'][f'test{x}'] = {
                    'feature': test[0],
                    'comp': test[1],
                    'val': test[2]
                }
                test_buffer[x] = {
                    'feature': test[0],
                    'comp': test[1],
                    'val': test[2]
                }
                # if column indicator is gt 1
                # copy preceeding tests to row dict from buffer
                if x > 1:
                    for i in range(1, x):
                        self._rows[row_count]['tests'][f'test{i}'] = test_buffer[i].copy()

        # finally, in source parsing
        # store max column count
        self._width = column_count

    @property
    def n_tests(self):
        """The number of tests in a given source"""
        if not self._width:
            return 0
        else:
            return self._width - 1

    @property
    def n_rows(self):
        if self._rows:
            return len(self._rows) - 1
        else:
            return 0

    def get_test(self, i_row: int, j_test: int, as_formula=False) -> str:
        """Returns copy of test dict indexed with row i and test j."""
        row_range = range(1, self.n_rows + 1)
        test_range = range(1, self.n_tests + 1)
        if i_row not in row_range:
            raise IndexError('Row index out of bounds.')
        if j_test not in test_range:
            raise IndexError('Test index out of bounds.')
        test_key = f'test{j_test}'
        default_if_missing = {
            'feature': None,
            'comp': None,
            'val': 1.0
        }
        dict_ptr = self._rows[i_row]['tests'].get(test_key, default_if_missing)
        if not as_formula:
            return dict_ptr.copy()
        else:
            if not dict_ptr['feature']:
                feature = ""
            else:
                feature = dict_ptr['feature']
            if not dict_ptr['comp']:
                comp = ""
            elif dict_ptr['comp'] == "==":
                comp = "="
            else:
                comp = dict_ptr['comp']
            val = dict_ptr['val']
            return f'={feature}{comp}{val}'

    def get_result(self, i_row: int) -> Union[float, None]:
        """Returns the result of row i ."""
        return self._rows[i_row]['result']

    def get_features(self) -> List[str]:
        return list(self._features)