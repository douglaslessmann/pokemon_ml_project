# Pokemon ML Project

## What should I read before cloning this repo?

This is an example project to undestand how to work with Kedro and MLFlow for machine learning projects. If you are new to Kedro and MLFlow, I highly recommend that you follow these getting started tutorials:

 * [Kedro](https://kedro.readthedocs.io/en/stable/02_get_started/01_prerequisites.html)
 * [MLFlow (with kedro-mlflow)](https://kedro-mlflow.readthedocs.io/en/stable/source/03_getting_started/index.html)

Also, to uderestand why they existe, I suggest this [video](https://www.youtube.com/watch?v=ZPxuohy5SoU&ab_channel=PyData). 

## Data used in this project

In this project, there are two datasets:

 * [The Complete Pokemon Dataset](https://www.kaggle.com/rounakbanik/pokemon). This dataset contains all pokemon stats, which we will use to create our models.
 * [Pokemon image dataset](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types). From this repo, we wills use the images when reporting our models precision.

## Goal of the project

The mains goal of this project is to help undestarnd how Kedro and MLFLow make your life a lot easier when working in a machine learning project that needes to be reproductible, matainbale e with tracking of the models metrics.

The ideia here is to classifie a Pokemon type based on his statics, such as Life, Attack, Defense. This ideia was inspired by this [Kaggle notebook](https://www.kaggle.com/ericazhou/pokemon-type-classification).

## Project dependencies

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
