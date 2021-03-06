# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._



### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/Gasia44/project-structure


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── Makefile               <- Makefile with commands like `make data` or `make train`
├── README.md              <- The top-level README for developers using this project.
├── data
│   ├── interim            <- Intermediate data that has been transformed.
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
│
├── models                 <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks              <- Jupyter notebooks
│
├── references             <- Data dictionaries, manuals, papers, and all other explanatory materials.
│
├── reports                <- Generated analysis as docs, HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── sql                    <- sql queries in .sql files
│
└── src                    <- Source code for use in this project.
    ├── __init__.py        <- Makes src a Python module
    │
    ├── data               <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features           <- Scripts to turn raw data into features for modeling
    │   ├── build_features.py
    │   └── preprocess.py  <- an interface to preprocess different tables/parts
    │
    ├── models             <- Scripts to train models and then use trained models to make predictions 
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── read_data.py       <- python script to read data in parallel


```


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
