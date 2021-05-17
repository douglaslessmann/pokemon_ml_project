from kedro.pipeline import Pipeline, node

from .nodes import save_indicium_predictor


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=save_indicium_predictor,
                name="save_indicium_predictor",
                inputs=[
                    "primary_type_classifier",
                    "label_encoder",
                    "pokemon_database_best_generations_with_images"
                ],
                outputs="IndiciumPredictor"
            )
        ]
    )
