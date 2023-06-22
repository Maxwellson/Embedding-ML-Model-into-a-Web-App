# Embedding-ML-Model-into-a-Web-App

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)



# Introduction

Fast API is a Python web framework use to build APIs quickly and efficiently. It acts as a bridge between the machine learning (ML) model and the app. With Fast API, you can analyse data quickly, efficiently, securely, by assessing automatic documentation.

# Project Description

Sepsis is a critical health condition which compromises the immune system instigating a malfunctioning of vital organs in the body. Damage to vital organs may occur as a result of a dramatic drop in blood pressure (septic shock) with its severity leading to death. Most people recover from mild sepsis, but the mortality rate for septic shock is about 30-40%. Early diagnosis of sepsis increases one's chances of survival and having foundational knowledge of the symptoms and triggers can help with early detection and reduce the mortality rate of sepsis.
As a biologist and a data scientist, it is fascinating to understand the proclivity of a patient getting sepsis from previous patient data. This project did just that by using the CRISP-DM framework.
## Data
Two csv files were downloaded: a train and test dataset.

The components of the data included; ID - number to represent patient ID, PRG - Plasma glucose, PL - Blood Work Result-1 (mu U/ml), PR - Blood Pressure (mm Hg), SK - Blood Work Result-2 (mm),TS - Blood Work Result-3 (mu U/ml), M11 - Body mass index (weight in kg/(height in m)²), BD2 - Blood Work Result-4 (mu U/ml), Age - Patient’s age (years), Insurance - If a patient holds a valid insurance card, Sepsis - Positive: if a patient in ICU will develop sepsis/Negative: otherwise.

# Structure
The directory contains app sub directories and a dataset for Sepsis :

1. [dev](D:\LP6\Embedding-ML-Model-into-a-Web-App\dev) folder model contains the model used for predicting , wether a person is suffering from sepsis or not, 6 hours before the onset. It also contains the files for all the pre- processing done. 
2. [src](D:\LP6\Embedding-ML-Model-into-a-Web-App\src) folder conains the fastapi app, requirements and the dockerfiles with its dependencies.

## Setup

To set up the project environment, follow these steps:

You need [`Python3`](https://www.python.org/) on your system to setup this app.

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  


# Modelling
![image](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App/assets/106244819/30187632-d39b-4779-983f-cfd1c19b6a01) 

![image](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App/assets/106244819/a11e9ab1-dec4-4940-b8fd-0121d9d54fe9)

![image](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App/assets/106244819/638ca031-01d7-49c0-b208-0afb0e940d72)


# Deployment 
![image](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App/assets/106244819/eec68426-15c1-461a-9033-4876431f4b8e)

![image](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App/assets/106244819/2a532965-d20d-48dd-b47c-f1c120186efc)

# Resources

Here are some resources you could explore to get a good understanding of FastAPI :
1. https://medium.com/themlblog/splitting-csv-into-train-and-test-data-1407a063dd74 
2. https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568 
3. https://medium.com/@robert.salgado/multiclass-text-classification-from-start-to-finish-f616a8642538
4. https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
5. https://www.districtdatalabs.com/text-analytics-with-yellowbrick
6. [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
7. [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
8. [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
9. [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

# Article and deployed app
https://medium.com/@cnorkplim/am-i-vulnerable-to-sepsis-a-data-analyst-perspective-4d31d8a9373c

https://huggingface.co/spaces/lindaclara22/Sepssis

# Author
Linda Adzigbli
