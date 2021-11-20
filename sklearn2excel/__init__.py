"""A Python package to facilitate Scikit-learn decision tree export to Excel."""
__version__ = "0.1.1"
__all__ = [
    "DecisionTreeTable",
    "export_to_textfile",
    "parse_file_to_list",
    "create_xlfile",
    "export_to_xlsx"
]

from .core import (
    Union, 
    DecisionTreeTable, 
    List
)
from .helpers import (
    BaseDecisionTree,
    Path,
    export_to_textfile,
    parse_file_to_list,
    create_xlfile,
    get_data_target_and_features,
)


def export_to_xlsx(
        decision_trees: Union[List[BaseDecisionTree], BaseDecisionTree],
        features: List[str],
        full_path: Path = Path.cwd() / "output.xlsx") -> None:
    """
    Usage:
        sklearn2excel.export_to_xlsx(sklearn_decisiontree)
            or
        sklearn2excel.export_to_xlsx(sklearn_ensemble.estimators_)
    """
    if issubclass(type(decision_trees), BaseDecisionTree):
        dts = list(decision_trees)
    elif isinstance(decision_trees, List):
        if all([issubclass(type(x), BaseDecisionTree) for x in decision_trees]):
            dts = decision_trees
    else:
        raise ValueError("Parameter :decision_trees: should be subclass of " + \
                         "BaseDecisionTree or a List thereof.")
    if not isinstance(features, List):
        raise ValueError("""Parameter :features: mus be a List of feature labels as strings.""")
    elif not all([isinstance(x, str) for x in features]):
        raise ValueError("""Parameter :features: must only contain feature labels as strings.""")

    list_of_lists = export_to_textfile(dts, Path(), features, in_memory=True)
    #print(list_of_lists[-1])
    dtt = DecisionTreeTable(list_of_lists)
    create_xlfile(dtt, full_path)
