# -*- coding: utf-8 -*-
"""Deploying a Machine Learning Model to MS Power BI
   By Sam Faraday
""
from pycaret.classification import load_model, predict_model
model = load_model('E:\python_dev\powerbi\ML_Pycaret_customer_churn')
dataset2 = dataset.copy()
dataset2["Label"] = ""
dataset.drop(['customerID','TotalCharges'], axis=1, inplace=True)
dataset = predict_model(model, data = dataset)
for i in dataset.index:
     dataset2.at[i, "Label"] = dataset['Label'][i]
     dataset2.at[i, "Score"] = dataset['Score'][i]
