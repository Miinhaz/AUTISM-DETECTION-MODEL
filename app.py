import uvicorn
from fastapi import FastAPI
from ASDs import ASD
import pickle


#create app object
app= FastAPI()
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#index routes, index page
@app.get('/')
def index():
    return{'message:' 'hi, my friend'}


#route with a parameter
@app.get('/{name}')
def get_name(name: str):
    return{'welcome here':f'{name}'}

#expose the prediction functionality; make a prediction from the json data and return the predicted asd
@app.post('/predict')
def predict_asd(data:ASD):
    data=data.dict()
    A1=data['Does_your_child_look_at_you_when_you_call_his_name']    
    A2=data['How_easy_is_it_for_you_to_get_eye_contact_with_your_child']
    A3=data['Does_your_child_point_to_indicate_that_he_wants_something']
    A4=data['Does_your_child_point_to_indicate_what_he_want']
    A5=data['Does_your_child_point_to_share_interest_with_you']
    A6=data['Does_your_child_follow_where_you_are_looking']
    A7=data['if_you_or_somweone_in_the_family_is_visibly_upset_does_your_child_show_sign_to_comfort_them']
    A8=data['Would_you_describe_your_childs_first_word_as_typical_or_unusual']
    A9=data['Does_your_child_use_simple_gestures_like_waving_goodbye']
    A10=data['Does_your_child_stare_at_nothing_with_no_apparent_purpose']
    Age_Mons=data['Age_Mons']
    Sex=data['Sex']
    Ethnicity=data['Ethnicity']
    #Ethnicity- White European/asian/middle eastern/south asian/black/Hispanic/Others/Latino/mixed/Pacific/Native Indian
    Jaundice=data['Jaundice']
    Family_mem_with_ASD=data['Family_mem_with_ASD']
    Who_completed_the_test=data['Who_completed_the_test']
    classifier.predict([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Age_Mons,Sex,Ethnicity,Jaundice,Family_mem_with_ASD, Who_completed_the_test]])
    prediction=classifier.predict([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Age_Mons,Sex,Ethnicity,Jaundice,Family_mem_with_ASD, Who_completed_the_test]])
    if (prediction[0]>0.5):
        prediction="ASD"
    else:
        prediction="No ASD"
    return{
        'prediction':prediction
        }

#run the api in unicorn
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
#python -m uvicorn app:app --reload    







