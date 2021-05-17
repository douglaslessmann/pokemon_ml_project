"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import Pipeline, node

from .nodes import clean_pokemon_database, add_pokemon_image


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                clean_pokemon_database,
                ["pokemon_database", "params:pokemon_best_generations"],
                'pokemon_database_best_generations',
            ),
            node(
                add_pokemon_image,
                ['pokemon_database_best_generations'],
                'pokemon_database_best_generations_with_images'
            )
        ]
    )
