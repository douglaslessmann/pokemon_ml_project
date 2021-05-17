import logging
import pandas as pd
import numpy as np
from typing import Any, Dict
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline as skl_pipeline
from pokemon_ml_project.helpers.helper_functions import model_from_string

log = logging.getLogger(__name__)


def split_data(
    df: pd.DataFrame,
    test_data_ratio: float,
    random_state: int = 1307
) -> Dict[str, Any]:
    """Node for splitting the data into train and test set
    """
    y = df.iloc[:, 0]
    X = df.iloc[:, 1:]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_data_ratio, random_state=random_state, stratify=y
        )

    # When returning many variables, it is a good practice to give them names:
    return dict(
        train_x=X_train,
        test_x=X_test,
        train_y=y_train,
        test_y=y_test,
    )


def fit_best_model(X_train, y_train, X_test, y_test, models, SEED=0):

    # Droping name and filepath, that are using for reporting only
    X_train.drop(['name', 'filepath'], axis='columns', inplace=True)
    X_test.drop(['name', 'filepath'], axis='columns', inplace=True)

    # Adding PCA to our pipeline & seting number of folds
    pca = PCA(n_components=20, random_state=SEED)

    kfold = KFold(n_splits=3, shuffle=True, random_state=SEED)

    for i, model in enumerate(models.keys()):

        classifier = model_from_string(models[model]['classifier'])

        classifier_grid = GridSearchCV(
            estimator=classifier,
            param_grid=models[model]['params'],
            cv=kfold, n_jobs=-1,
            scoring='accuracy',
            verbose=2)

        pipe = skl_pipeline([
            ('pca', pca),
            ('classifier', classifier_grid)
        ])

        pipe.fit(X_train, np.ravel(y_train))

        score = accuracy_score(y_test, pipe.predict(X_test))
        score_fit = accuracy_score(y_train, pipe.predict(X_train))

        # check if it is better than classifier
        if i == 0:
            best_classifier = pipe['classifier'].best_estimator_
            best_score = score
        elif (score > best_score) and (score < score_fit):
            best_classifier = pipe['classifier'].best_estimator_
            best_score = score

    # return pipeline with best classifier
    pipe = skl_pipeline([
        ('pca', pca),
        ('classifier', best_classifier),
    ])

    best_score = accuracy_score(y_test, pipe.predict(X_test))

    log.info(f"Best classifier: {best_classifier}")
    log.info(f"Best scorer: {np.round(best_score, 4)}")

    pipe.fit(X_train, np.ravel(y_train))

    return pipe, pd.DataFrame({'model': [str(pipe[1])]})
