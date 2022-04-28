"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from pokemon_ml_project.pipelines import pre_processing as pp
from pokemon_ml_project.pipelines import data_engineering as de
from pokemon_ml_project.pipelines import data_science as ds
from pokemon_ml_project.pipelines import model_metrics as mm
from pokemon_ml_project.pipelines import api_pipeline as api


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    pre_processing_pipeline = pp.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    model_metrics_pipeline = mm.create_pipeline()
    api_pipeline = api.create_pipeline()

    return {
        "pp": pre_processing_pipeline,
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "mm": model_metrics_pipeline,
        "api_pipeline": api_pipeline,
        "__default__": (
            pre_processing_pipeline
            + data_engineering_pipeline
            + data_science_pipeline
            + model_metrics_pipeline
            + api_pipeline
        ),
    }
