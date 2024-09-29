# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:42:37 2022

@author: Miinhaz
"""
import numpy as np
import pickle

#LOADING THE SAVED MODEL
loaded_model=pickle.load(open('J:/project 2.0/trained_model.sav','rb'))
input_data=(	
0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	36,	1,	6,	0,	0,	4
)
#input data as numpy array
input_data_as_np_array=np.asarray(input_data)
#reshape the array for one instnce
input_data_reshaped=input_data_as_np_array.reshape(1,-1)

#scaling the data for one instance
#this will need if we use standard scalling
#std_data=sc.transform(input_data_reshaped)

prediction=loaded_model.predict(input_data_reshaped)
print('The prediction is: ',prediction)
#print('Here--->\n [1] Denotes ASD \n [0] Denotes No ASD')

if (prediction[0] == 1):
    print('The Child has ASD')
else:
    print('The Child has no ASD')
