# Pokemon ML Project

Repo used for training purposes at [Indicum](https://indicium.tech/).

## What should I read before cloning this repo?

This is an example project to understand how to work with Kedro and MLFlow for machine learning projects. If you are new to Kedro and MLFlow, I highly recommend that you follow these getting started tutorials:

 * [Kedro](https://kedro.readthedocs.io/en/stable/02_get_started/01_prerequisites.html)
 * [MLFlow (with kedro-mlflow)](https://kedro-mlflow.readthedocs.io/en/stable/source/03_getting_started/index.html)

Also, to understand why they exist I suggest this [video](https://www.youtube.com/watch?v=ZPxuohy5SoU&ab_channel=PyData). 

## Data used in this project

In this project, there are two datasets:

 * [The Complete Pokemon Dataset](https://www.kaggle.com/rounakbanik/pokemon). This dataset contains all pokemon stats, which we will use to create our models.
 * [Pokemon image dataset](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types). From this repo, we will use the images when reporting our models precision.

In order to reproduce this project you will need to have in `data/01_raw/` the `pokemon.csv` from The Complete Pokemon Dataset and a `images` folder, with all pokemon images.

![image (21)](https://user-images.githubusercontent.com/62858527/118688408-6a5b7980-b7dc-11eb-8711-5bfda585b7ff.png)

## Goal of the project

The mains goal of this project is to help understand how Kedro and MLFLow make your life a lot easier when working in a machine learning project that needs to be reproducible, maintainable e with tracking of the models metrics.

The idea here is to classify a Pokemon type based on his statics, such as Life, Attack, Defense. This idea was inspired by this [Kaggle notebook](https://www.kaggle.com/ericazhou/pokemon-type-classification).

## Project dependencies

This project was created using Kedro 0.17.3. To install, run:

```
pip install kedro==0.17.3
```

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

## How to install dependencies

To install them, run:

```
kedro install
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```
### Pipeline structure

The pipeline structure of this project is based on what we think is the optimal way of working in ML projects. Here we have a brief description of what expect in each pipeline.

  1) **Pre-processing pipeline**: basic data manipulation such as rename columns, filter rows, select, cast data type.
  2) **Data engineering pipeline**: create new features, handling the missing data, here we have more complex data manipulations
  3) **Data science pipeline**: train models, while testing different techniques and hyperparameters tuning. If you are working on a project with multiple objectives, I suggest you rename your pipeline based on your model. Let's suppose we wanted also to predict the pokemon attack. Then, we would have a pipeline named predict_primary_type and predict_attack if this was another objective, and the data science pipeline would be extinct.
  4) **Model metrics pipeline**: a pipeline to make report of our precision and register our metrics using MLFlow
  5) **Indicium predictor**: the optimal way that we developed at [Indicum](https://indicium.tech/) to use our models in API.


