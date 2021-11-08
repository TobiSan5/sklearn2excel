"""A Python package to facilitate Scikit-learn decision tree export to Excel."""
__version__ = "0.1.0"
__all__ = [
    "DecisionTreeTable",
    "export_decisiontrees_to_file",
    "parse_file_to_list",
    "create_xlfile",
]

from typing import Sequence
from .core import Union, DecisionTreeTable
from .helpers import (
    BaseDecisionTree,
    Path,
    export_decisiontrees_to_file,
    parse_file_to_list,
    create_xlfile,
)


def export_to_xlsx(
        decision_trees: Union[Sequence[BaseDecisionTree], BaseDecisionTree],
        features: Sequence[str],
        full_path: Path(Path.cwd() / "output.xlsx")) -> None:
    """
    Usage:
        sklearn2excel.export_to_xlsx(sklearn_decisiontree)
            or
        sklearn2excel.export_to_xlsx(sklearn_ensemble.estimators_)
    """
    if issubclass(decision_trees, BaseDecisionTree):
        dts = list(decision_trees)
    elif isinstance(decision_trees, Sequence):
        if all([issubclass(x, BaseDecisionTree) for x in decision_trees]):
            dts = decision_trees
    else:
        raise ValueError("Parameter :decision_trees: should be subclass of " + \
                         "BaseDecisionTree or a sequence thereof.")
    if not isinstance(features, Sequence):
        raise ValueError("""Parameter :features: mus be a sequence of feature labels as strings.""")
    elif not all([isinstance(x, str) for x in features]):
        raise ValueError("""Parameter :features: must only contain feature labels as strings.""")

    list_of_lists = export_decisiontrees_to_file(dts, Path(), features, in_memory=True)
    dtt = DecisionTreeTable(list_of_lists, )
    create_xlfile(dtt, full_path)
