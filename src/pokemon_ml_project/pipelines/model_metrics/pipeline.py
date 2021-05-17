"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import Pipeline, node

from .nodes import display_by_type, classification_accurracy

POKEMON_TYPES = [
    'ice', 'water', 'grass', 'fire', 'psychic', 'rock', 'normal', 'ground', 'dragon',
    'fairy', 'bug', 'fighting', 'dark', 'ghost', 'poison', 'electric', 'steel', 'flying'
]


def create_pipeline(**kwargs):
    node_list = []
    for pokemon_type in POKEMON_TYPES:
        node_list.append(
            node(
                name=pokemon_type,
                func=display_by_type,
                inputs={
                    'pokemon_type': f"params:pokemon_type_{pokemon_type}",
                    'num': 'params:pokemon_num',
                    'X_test': 'X_test',
                    'y_test': 'y_test',
                    'classifier_model': 'primary_type_classifier',
                    'label_encoder': 'label_encoder',
                    'color_dict': 'params:color_dict'
                },
                outputs=f"{pokemon_type}_validation_plot"
            )
        )

    node_list.append(
            node(
                func=classification_accurracy,
                inputs=['X_test', 'y_test', 'primary_type_classifier'],
                outputs="classification_metrics",
                name="log_metrics"
            )
        )

    return Pipeline(nodes=(node_list))
