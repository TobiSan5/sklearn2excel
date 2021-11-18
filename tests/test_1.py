import os
from time import sleep
from pathlib import Path
import unittest
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn2excel import (
    export_to_xlsx,
    export_to_textfile,
    BaseDecisionTree,
    DecisionTreeTable,
    parse_file_to_list,
    create_xlfile,
    List,
    get_data_target_and_features
)


class TestData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bunch = get_data_target_and_features()
        cls.data = bunch.data
        cls.target = bunch.target
        cls.n_features = 4
        cls.features = bunch.feature_names[:cls.n_features]
        cls.y = LabelEncoder().fit_transform(cls.target)
        cls.rf = RandomForestRegressor(n_estimators=10, min_samples_leaf=2)\
            .fit(cls.data[cls.features], cls.y)
        cls.rfc = RandomForestClassifier(n_estimators=10, min_samples_leaf=2)\
            .fit(cls.data[cls.features], cls.y)

    def test_subclass(self):
        self.assertTrue(issubclass(type(self.rf.estimators_[0]), BaseDecisionTree))
        self.assertTrue(
            all(issubclass(type(x), BaseDecisionTree)
                for x in self.rf.estimators_))

    def test_export(self):
        # testing export to textfile from model
        path_r = Path.cwd() / 'randomforest_r_test.txt'
        path_c = Path.cwd() / 'randomforest_c_test.txt'
        path_xlsx = Path.cwd() / "test_export_parse_export.xlsx"
        path_inmemory_xlsx = Path.cwd() / 'test_export_to_xlsx.xlsx'
        path_r.write_text('')
        path_c.write_text('')
        export_to_textfile(self.rf.estimators_, path_r, self.features)
        export_to_textfile(self.rfc.estimators_, path_c, self.features)
        self.assertIn("|   |   |   |--- value: [1.00]", path_r.read_text())
        self.assertIn("|   |   |   |--- class: 1.0", path_c.read_text())

        # testing parsing and exporting through instance of DecicionTreeTable
        lol = parse_file_to_list(path_r)
        print(lol[0])
        sleep(1)
        self.assertTrue(path_r.exists())
        self.assertTrue(isinstance(lol, List))
        dtt = DecisionTreeTable(lol)
        self.assertEqual(self.n_features, len(dtt.get_features()))
        print(f'dtt features: {dtt.get_features()}')
        if path_xlsx.exists():
            os.remove(path_xlsx)
        create_xlfile(dtt, path_xlsx)
        sleep(1)
        self.assertTrue(path_xlsx.exists())
        print(dtt.get_test(1, 1, as_formula=True))
        print(dtt.get_test(1, 2, as_formula=True))
        print(f'test width: {dtt.n_tests}')
        print(f'rows: {dtt.n_rows}')

        # testing direct function export_to_xlsx (not dependent on textfile)
        if path_inmemory_xlsx.exists():
            os.remove(path_inmemory_xlsx)
        export_to_xlsx(self.rf.estimators_, self.features, path_inmemory_xlsx)
        sleep(1)
        self.assertTrue(path_inmemory_xlsx.exists())





if __name__ == '__main__':
    unittest.main()

