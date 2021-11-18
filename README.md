# sklearn2excel
> Bringing Scikit-learn decision trees to Excel

<!--
[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]
-->

With this Python package, one can make a trained machine learning model
accessible to others without having to deploy it as a service.
More specifically, one can export a Scikit-learn decision 
tree or random forest model to a Excel workbook.
All decision chains in the model will be represented within a single 
table and feature values can be tested for an average prediction.

<!-- 
Screenshot: 
![](header.png) 
-->

### Project overview
Version: 0.1.0
- helpers module
  - [X] export_to_textfile
    - [X] A wrapper function for sklearn.tree.export_to_text ()
    - [X] Detects maximum tree depth and applies this parameter
  - [X] create_xlfile
    - [X] Writes a DecisionTreeTable object to a Excel sheet
    - [X] Write features and an initial value of 1 to another sheet
- core module
  - [X] DecisionTreeTable
    - [X] A class that can be instantiated with a text file
    - [X] Transforms and represent decisions trees in a datastructure
    - [X] Exposed properties to get info about the structure
    - [X] Exposed methods to get tests and results as indexed rows
    - [X] TODO: Handle classifier-type decision trees
- tests
  - [ ] Full test coverage

## Installation

```sh
pip install sklearn2excel
```
Installation will install scikit-learn and XlsxWriter as well.

## Usage example

<!--code block with a few useful and motivating examples. Again you’d lay out exactly what people need to type into 
their shell -->
```python
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import sklear2excel as s2e


# fetch Scikit-learn wine example data as
# sklearn.utils.Bunch object
# and prepare example model from
# sklearn.ensemble.RandomForestClassifier
# RandomForestRegressor or any classifier/regressor
# subtype of BaseDecisionTree could be used
bunch = s2e.get_data_target_and_features()
wine_data = bunch.data
wine_target = bunch.target
wine_features = bunch.feature_names[:4]
X = wine_data[wine_features]
y = LabelEncoder().fit_transform(wine_target)
clf_model = RandomForestClassifier(
  n_estimators=10, 
  min_samples_leaf=2
).fit(X, y)

path_xlsx = Path.cwd() / "excel_output.xlsx"
path_txt = Path.cwd() / "text_output.txt"

# export model as text file with use of 
# sklearn export function
# first param single or ensemble of decision trees
s2e.export_to_textfile(
  clf_model.estimators_,  # ensemble of decision trees
  path_txt,
  wine_features
)

# export model as Excel file
# features written to Front sheet with initial value 1.0
# decision trees written to 2nd sheet
s2e.export_to_xlsx(
  clf_model.estimators_,
  wine_features,
  path_xlsx
)
```


## Development setup

<!--describe how to install all development dependencies and how to run an automated 
test-suite-->
- Flit ~3.4

## Release History
<!--
* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
-->

- 0.1.0
  - First proper release
  - NEW: direct function `export_to_xlsx()`
  - CHANGE: functions and class available at package-level
- 0.0.1
  - Work in progress


## Meta

Torbjørn Wikestad – [@TWikestad](https://twitter.com/twikestad) – torbjorn.wikestad@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/tobisan5/github-link](https://github.com/tobisan5/)


## Contributing

1. Fork it (<https://github.com/tobisan5/sklearn2excel/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[wiki]: https://github.com/yourname/yourproject/wiki
