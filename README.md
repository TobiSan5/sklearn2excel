# Decision tree to Excel

## Rationale

Scikit-learn is a great Python package for machine learning,
and is quite accessible, also for those with limited 
knowledge of Python and data science. However,
when it comes to accesibility, nothing beats grand old
Excel, as the base calculation tool for many engineers.
It would be nice to have a set of tools to export
machine learning models from Scikit-learn to Excel.

## Goals

- [X] Export a model based on sklearn.ensemble.RandomForestRegressor
to a text file. This was achieved using sklearn.tree.export_to_text
  
- [ ] Define a DecisionTreeText class that can be instatiated
with a text file exported from Scikit-learn. The text file
  should be traversed, and transformed to a datastructure (dictionary)
  consisting of decision chains, consisting of logic steps
  and a predicted value.
