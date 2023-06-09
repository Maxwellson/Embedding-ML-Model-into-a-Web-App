# Embedding-ML-Model-into-a-Web-App

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Introduction

Fast API is a Python web framework use to build APIs quickly and efficiently. It acts as a bridge between the machine learning (ML) model and the app. With Fast API, you can analyse data quickly, efficiently, securely, by assessing automatic documentation.


## Description

You will have a minimal interface demo with [Gradio](https://gradio.app/) & [Streamlit](https://streamlit.io/), this will just serve you to make sure that everything works correctly. Then, you will have to make your own interfaces, those allowing you to interact with a Machine Learning model, that is to say:
- Pass values through the interface;
- Recover these values in backend;
- Apply the necessary processing;
- Submit the previously processed values to the ML model to make the predictions;
- Process the predictions obtained and display them on the interface.


## Installation

You have two ways in order to setup and run this project.

### Setup

o set up the project environment, follow these steps:

You need [`Python3`](https://www.python.org/) on your system to setup this app. Then you can clone this repo ['FastAPI'](https://github.com/Norkplim22/Embedding-ML-Model-into-a-Web-App.git) and follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  


**NB:** For MacOs users, please install `Xcode` if you have an issue.

- Run the demo apps (being at the repository root):

  Gradio: 
  
    For development

      gradio src/app.py
    
    For normal deployment/execution

      python src/app.py  

  - Go to your browser at the following address :
        
      http://localhost:7860

## Modelling
<table>
    <tr>
        <th> Modelling Framework </th>
    </tr>
    <tr>
        <td><img src="D:\LP6\Embedding-ML-Model-into-a-Web-App\images\Modelling.png"/></td>
    </tr>
</table>

7 directories, 4 files
```
## Screenshots

<table>
    <tr>
        <th> FastAPI </th>
    </tr>
    <tr>
        <td><img src="D:\LP6\Embedding-ML-Model-into-a-Web-App\images\fastapi1.jpg"/></td>
    </tr>
</table>

## Resources

Here are some resources you could explore to get a good understanding of FastAPI :
https://medium.com/themlblog/splitting-csv-into-train-and-test-data-1407a063dd74 
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568 
https://medium.com/@robert.salgado/multiclass-text-classification-from-start-to-finish-f616a8642538
https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
https://www.districtdatalabs.com/text-analytics-with-yellowbrick


## Author
Linda Adzigbli