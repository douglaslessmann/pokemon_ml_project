"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import Pipeline, node

from .nodes import create_model_input


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                create_model_input,
                ['pokemon_database_best_generations_with_images'],
                ['model_input', 'label_encoder']
            )
        ]
    )
