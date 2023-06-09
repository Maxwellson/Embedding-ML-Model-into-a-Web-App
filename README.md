# Embedding-ML-Model-into-a-Web-App
!['image'](https://www.bing.com/images/search?view=detailV2&ccid=sNQ%2bJuRy&id=E20302212CAD7FA53ED15FE7DB91B723F128F1D3&thid=OIP.sNQ-JuRyaEWorqPyrLxmMQHaEK&mediaurl=https%3a%2f%2famalgjose.files.wordpress.com%2f2021%2f02%2ffast_api_ppt.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.b0d43e26e4726845a8aea3f2acbc6631%3frik%3d0%252fEo8SO3kdvnXw%26pid%3dImgRaw%26r%3d0&exph=720&expw=1280&q=fastapi&simid=607986268060862822&FORM=IRPRST&ck=A704608081331589ABB1F8F82AC39324&selectedIndex=3)

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Introduction

Fast API is a Python web framework use to build APIs quickly and efficiently. It acts as a bridge between the machine learning (ML) model and the app. With Fast API, you can analyse data quickly, efficiently, securely, by assessing automatic documentation.



## Project Description

Sepsis is a critical health condition which compromises the immune system instigating a malfunctioning of vital organs in the body. Damage to vital organs may occur as a result of a dramatic drop in blood pressure (septic shock) with its severity leading to death. Most people recover from mild sepsis, but the mortality rate for septic shock is about 30-40%. Early diagnosis of sepsis increases one's chances of survival and having foundational knowledge of the symptoms and triggers can help with early detection and reduce the mortality rate of sepsis.

### Data
Two csv files were downloaded: a train and test dataset.

The components of the data included; ID - number to represent patient ID, PRG - Plasma glucose, PL - Blood Work Result-1 (mu U/ml), PR - Blood Pressure (mm Hg), SK - Blood Work Result-2 (mm),TS - Blood Work Result-3 (mu U/ml), M11 - Body mass index (weight in kg/(height in m)²), BD2 - Blood Work Result-4 (mu U/ml), Age - Patient’s age (years), Insurance - If a patient holds a valid insurance card, Sepsis - Positive: if a patient in ICU will develop sepsis/Negative: otherwise.

# Structure
The directory contains app sub directories and a dataset for Sepsis :

1. [dev](D:\LP6\Embedding-ML-Model-into-a-Web-App\dev) folder model contains the model used for predicting , wether a person is suffering from sepsis or not, 6 hours before the onset. It also contains the files for all the pre- processing done. 
2. [src](D:\LP6\Embedding-ML-Model-into-a-Web-App\src) folder conains the fastapi app, requirements and the dockerfiles with its dependencies.

### Setup

To set up the project environment, follow these steps:

You need [`Python3`](https://www.python.org/) on your system to setup this app. Then you can clone this repo ['FastAPI'](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App.git) and follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  


## Modelling
!['ML Framework'](D:\LP6\Embedding-ML-Model-into-a-Web-App\images\Modelling.png) 

!['Metrics trimed data']
(D:\LP6\Embedding-ML-Model-into-a-Web-App\images\metric without outliers.jpg)
![Metrics untrimmed data](D:\LP6\Embedding-ML-Model-into-a-Web-App\images\metric, with outlier.jpg)

```
## Deployment 


## Resources

Here are some resources you could explore to get a good understanding of FastAPI :
https://medium.com/themlblog/splitting-csv-into-train-and-test-data-1407a063dd74 
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568 
https://medium.com/@robert.salgado/multiclass-text-classification-from-start-to-finish-f616a8642538
https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
https://www.districtdatalabs.com/text-analytics-with-yellowbrick
[FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

## Author
Linda Adzigbli