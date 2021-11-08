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
All decision chains in model will be represented within a single 
table and feature values can be tested for an average result.

<!-- 
Screenshot: 
![](header.png) 
-->

### Project overview
Version: 0.1.0
- helpers module
  - [X] export_decisiontrees_to_file
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
import sklear2excel
output_path = Path("./excel_file.xlsx")
# Example using sklearn.ensemble.RandomForestRegressor model
# (the model is trained)
sklearn2excel.export_to_xlsx(randomforestmodel.estimators_, feature_names_list, output_path)
# Example with single sklearn.tree.DecisionTreeRegressor model
sklearn2excel.export_to_xlsx(list(dt_model), feature_names_list, output_path)
```


## Development setup

<!--describe how to install all development dependencies and how to run an automated 
test-suite-->
No other development dependencies.

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
