from fastapi import FastAPI
import schemas
import pickle


app=FastAPI()

@app.get('/Bank_note')
def show():
    return 'Bank_authentification'

pickle_in=open('classifier.pkl','rb')
pred=pickle.load(pickle_in)

mp=['fraud','no fraud']
@app.post('/predict')
def predict(request:schemas.independent):
    res=pred.predict([[request.variance,request.skewness,request.curtosis,request.entropy]])

    return "The predicted class is : " + mp[int(res)]
    
    