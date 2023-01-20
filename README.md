# Packaging insurance claim model

The reason I make this repo is to practice about how to make **reusable code** from *jupyter notebooks* which perform EDA and modeling parts and make python packaging with that code which can install with **pip**.

## Steps I make through this repository

- **notebook**
    
    You can see the EDA, feature engineering and modeling notebook inside **notebook** folder. 

- **source code**

    You can see the main source code that make from above notebooks in **insurance_claim_model** folder.

Actually I didn't give much time to EDA and feature engineering parts because I want to emphasize to make the **well-structured code** with good practices like testing with **tox** and **pytest** and using lint tools.

- **Packaging**

    You can see **MANIFEST.in**, **pyproject.toml** and **setup.py** which are essential for python packaging.

The steps I make for this repo is that at first, I make EDA and modeling notebook. From these notebooks, I create the python files(.py). Then I carefully structure these codes, check the code quality with pytest and use the tools which can make the python code better with flake8, isort, black and mypy tools and finally make the python package from that code. You can see my python package in [here](https://pypi.org/project/insurance-claim-model/).

## About Dataset

The dataset I use in this repository is from [here](https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health). It is about insurance claim analysis from demographics and health factors. It is released on 2023. 

I make a regression model with random forest which can predict insurance claim from that dataset. 









