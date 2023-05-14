import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_test = pd.read_csv('D:\LP6\Embedding-ML-Model-into-a-Web-App\dataset\Paitients_Files_Test.csv')
df_train = pd.read_csv('D:\LP6\Embedding-ML-Model-into-a-Web-App\dataset\Paitients_Files_Train.csv')

df_test.shape, df_train.shape
df_train