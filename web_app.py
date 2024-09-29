# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:47:18 2022

@author: USER
"""

import numpy as np
import pickle
import streamlit as st

#LOADING THE SAVED MODEL
loaded_model=pickle.load(open('J:/project 2.0/trained_model.sav','rb'))

# creating a function for Prediction

def ASD_prediction(input_data):
    #input data as numpy array
    input_data_as_np_array=np.asarray(input_data)
    #reshape the array for one instnce
    input_data_reshaped=input_data_as_np_array.reshape(1,-1)


    prediction=loaded_model.predict(input_data_reshaped)
    print('The prediction is: ',prediction)

    if (prediction[0] == 1):
        return 'The Child has ASD'
    else:
        return 'The Child has no ASD'
        
def main():
    
    
    # giving a title
    st.title('ASD Prediction Web App')
    
    # getting the input data from the user
    A1=st.text_input('Does your child look at you when you call his/her name?')
    A2=st.text_input(' How easy is it for you to get eye contact with your child?')
    A3=st.text_input('Does your child point to indicate that he/she wants something?')
    A4=st.text_input('Does your child point to indicate what she/he want?')
    A5=st.text_input('Does your child point to share interest with you?')
    A6=st.text_input('Does your child follow where you are looking?')
    A7=st.text_input('if you or someone in the family is visibly upset does your child show sign to comfort them?')
    A8=st.text_input('Would you describe your childs first word as typical or unusual?')
    A9=st.text_input('Does your child use simple gestures like waving goodbye?')
    A10=st.text_input('Does your child stare at nothing with no apparent purpose?')
    Age_Mons=st.text_input('Age Month of your child')
    Sex=st.text_input('Sex of the child')
    Ethnicity=st.text_input('Ethnicity of the child')
    Jaundice=st.text_input('Does your child have Jaundice?')
    Family_mem_with_ASD=st.text_input('Is there any family member with ASD?')
    Who_completed_the_test=st.text_input('Who completed the test of ASD')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('ASD Test Result'):
        diagnosis = ASD_prediction([A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Age_Mons,Sex,Ethnicity,Jaundice,Family_mem_with_ASD, Who_completed_the_test])
       
       
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    #streamlit run "J:\project 2.0\web_app.py"