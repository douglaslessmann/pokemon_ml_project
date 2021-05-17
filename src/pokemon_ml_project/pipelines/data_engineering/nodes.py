import pandas as pd
import ast
from sklearn.preprocessing import LabelEncoder


def calculate_number_of_abilities(df):
    """Helper function to get size of list from the column
    'abilities', so we can know the number of abilities of the pokemon.
    This function will be used with and apply by row to the dataframe.
    """
    abilities = df['abilities']
    abilities_as_list = ast.literal_eval(abilities)
    number_of_abilities = len(abilities_as_list)
    return number_of_abilities


def create_model_input(
    df: pd.DataFrame,
    dependent_variable: str = 'primary_type'
):
    """Node for creating columns that will be used as model input.
    """

    # Encode string class values as integers
    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df['primary_type'])

    df['primary_type'] = label_encoder.transform(df['primary_type'])

    # Calculate the number of abilities
    df = df.assign(
        number_of_abilities=df.apply(
            calculate_number_of_abilities,
            axis=1
        )
    )

    # Create variable to indicate if pokemon is female
    df['is_female'] = 0
    df.loc[df.percentage_male == 0, 'is_female'] = 1

    # Numerical status columns
    numerical_stats_columns = [
        'base_total', 'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed',
        'height_m', 'weight_kg',  'number_of_abilities', 'is_female'
    ]

    # Againts columns
    against_columns = [col for col in df if col.startswith('against_')]

    # Select only columns that will be used in out model
    final_columns = [dependent_variable] + numerical_stats_columns + \
        against_columns + ['name', 'filepath']

    df = df[final_columns]

    return df, label_encoder
