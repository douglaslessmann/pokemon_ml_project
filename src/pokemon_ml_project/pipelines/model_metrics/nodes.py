import random
from matplotlib import image
from matplotlib import pyplot as plt
from typing import Dict, Union, List
from sklearn.metrics import accuracy_score


def get_filepaths(X_test, y_test_pop, pokemon_type, num):
    idxs = list(y_test_pop[y_test_pop == pokemon_type].index)
    if len(idxs) > num:
        idxs = random.sample(idxs, num)
    correct = y_test_pop[idxs]
    pokemon = list(X_test['filepath'][idxs])
    names = list(X_test['name'][idxs])
    return list(zip(pokemon, names, correct))


def display_by_type(
    pokemon_type,
    num,
    X_test,
    y_test,
    classifier_model,
    label_encoder,
    color_dict: dict,
    image_directory: str = './data/01_raw/images/'
):
    # Transforming y_test to text
    y_test_str = y_test.copy()

    y_test_str['primary_type'] = label_encoder.inverse_transform(
        y_test_str['primary_type']
    )

    y_test_pop = y_test_str.pop('primary_type')

    X_test_input = X_test.drop(['name', 'filepath'], axis='columns')

    y_pred_dt = classifier_model.predict(X_test_input)

    y_pred_dt_str = label_encoder.inverse_transform(y_pred_dt)

    # List with name, image filepath, true type and predicted type
    filepaths = []
    validation_pokemons = get_filepaths(X_test, y_test_pop, pokemon_type, num)
    filepaths.append(validation_pokemons)  # truth
    # model prediction
    validation_pokemons_names = [name[1] for name in validation_pokemons]

    X_validation_pokemons = X_test[X_test.name.isin(validation_pokemons_names)]

    validation_pokemons_pred = []

    for index, pokemon in enumerate(validation_pokemons):
        pokemon_name = pokemon[0]
        pokemon_image_filepath = pokemon[1]
        pokemon_type_i = y_pred_dt_str[X_validation_pokemons.index][index]
        pokemon_perd = tuple([pokemon_name, pokemon_image_filepath, pokemon_type_i])
        validation_pokemons_pred.append(pokemon_perd)

    filepaths.append(validation_pokemons_pred)

    cols = num
    rows = 2

    fig = plt.figure(figsize=(20, 12))
    plt.text(0.04, 0.7, 'ground\ntruth', fontsize=20, transform=plt.gcf().transFigure)
    plt.text(0.04, 0.275, 'prediction', fontsize=20, transform=plt.gcf().transFigure)
    plt.box(False)
    plt.xticks([])
    plt.yticks([])

    for i in range(rows):
        for j in range(cols):
            ax = fig.add_subplot(rows, cols, i*cols+j+1)
            if j >= len(filepaths[i]):
                plt.box(False)
                plt.xticks([])
                plt.yticks([])
                continue
            filepath, name, correct = filepaths[i][j]
            img = image.imread(image_directory+filepath)
            plt.imshow(img)
            plt.title(
                name + ': ' + correct,
                color=color_dict[correct],
                fontdict={'fontsize': 20}
            )
            plt.xticks([])
            plt.yticks([])

            if i == 0:
                spine_color = 'gray'
            elif correct == pokemon_type:
                spine_color = 'green'
            else:
                spine_color = 'red'
            for spine in ax.spines.values():
                spine.set_edgecolor(spine_color)
    return fig


def classification_accurracy(
    X_test, y_test, classifier_model
) -> Dict[str, Union[float, List[float]]]:

    X_test.drop(['name', 'filepath'], axis='columns', inplace=True)

    best_score = accuracy_score(y_test, classifier_model.predict(X_test))

    return {
        "accurracy": {"value": best_score, "step": 1}
    }
