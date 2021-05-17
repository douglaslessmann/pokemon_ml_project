import pandas as pd
import numpy as np


class IndiciumPredictor:
    def __init__(
        self,
        classifier_model,
        label_encoder
    ):
        self.classifier_model = classifier_model
        self.label_encoder = label_encoder

    def predict(self, info_API: dict):
        args = info_API

        df_args = pd.DataFrame({k: [v] for k, v in args.items()})

        class_prediction = self.classifier_model.predict(df_args)

        class_prediction_str = self.label_encoder.inverse_transform(class_prediction)

        return class_prediction_str


def save_indicium_predictor(
    classifier_model,
    label_encoder,
    pokemon_database
):
    predictor = IndiciumPredictor(classifier_model, label_encoder)

    if teste_predict_function(predictor, pokemon_database):
        return predictor
    raise "Alguma coisa deu errado"


def teste_predict_function(predictor, pokemon_database):
    info_API = {
        'base_total': 250.0,
        'attack': 50.0,
        'defense': 40.0,
        'hp': 50.0,
        'sp_attack': 30.0,
        'sp_defense': 30.0,
        'speed': 50.0,
        'height_m': 0.4,
        'weight_kg': 6.5,
        'number_of_abilities': 3.0,
        'is_female': 0.0,
        'against_bug': 1.0,
        'against_dark': 1.0,
        'against_dragon': 1.0,
        'against_electric': 0.0,
        'against_fairy': 1.0,
        'against_fight': 2.0,
        'against_fire': 2.0,
        'against_flying': 1.0,
        'against_ghost': 1.0,
        'against_grass': 2.0,
        'against_ground': 1.0,
        'against_ice': 1.0,
        'against_normal': 1.0,
        'against_poison': 0.5,
        'against_psychic': 1.0,
        'against_rock': 1.0,
        'against_steel': 2.0,
        'against_water': 2.0
    }

    results = predictor.predict(info_API)

    pokemon_types = pokemon_database['primary_type'].unique()

    if np.isin(results, pokemon_types):
        return True
    return False
