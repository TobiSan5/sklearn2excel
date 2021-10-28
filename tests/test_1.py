from pathlib import Path
import unittest
from helpers import get_data_target_and_features
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn2excel.helpers import export_decisiontrees_to_file


class TestData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bunch = get_data_target_and_features()
        cls.data = bunch.data
        cls.target = bunch.target
        cls.features = bunch.feature_names
        cls.y = LabelEncoder().fit_transform(cls.target)
        cls.rf = RandomForestRegressor(n_estimators=10)\
            .fit(cls.data[['alcohol', 'malic_acid', 'ash']], cls.y)
        path = Path.cwd() / 'randomforest_test.txt'
        export_decisiontrees_to_file(cls.rf.estimators_, path, ['alcohol', 'malic_acid', 'ash'])


    def test_something(self):
        self.assertEqual(len(self.features), 13)
        self.assertEqual(len(self.rf.estimators_), 10)
        self.assertEqual(Path(Path.cwd() / 'randomforest_test.txt').is_file(), True)


if __name__ == '__main__':
    unittest.main()

