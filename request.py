# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:07:39 2022

@author: USER
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())