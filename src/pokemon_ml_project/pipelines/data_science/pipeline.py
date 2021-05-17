"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import Pipeline, node

from .nodes import split_data, fit_best_model


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                split_data,
                {
                    "df": "model_input",
                    "test_data_ratio": "params:test_data_ratio"
                },
                {
                    "train_x": "X_train",
                    "train_y": "y_train",
                    "test_x": "X_test",
                    "test_y": "y_test",
                }
            ),
            node(
                fit_best_model,
                {
                    "X_train": 'X_train',
                    "y_train": 'y_train',
                    "X_test": 'X_test',
                    "y_test": 'y_test',
                    "models": "params:primary_type_models"
                },
                ['primary_type_classifier', 'model_name']
            )
        ]
    )
