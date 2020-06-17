{{cookiecutter.project_name}}
==============================

Project Organization
------------

    ├── Makefile               <- Makefile with commands like `make data` or `make train`
    ├── README.md              <- The top-level README for developers using this project.
    │
    ├── config                 <- Configurations in Json/Yaml format
    │
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
    

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
