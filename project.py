from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.metrics import accuracy_score
data=pd.read_excel(r"my.xlsx")
st.title("heart disease prediction :")
# print(data.columns)
X=data[['age', 'cp', 'trestbps', 'chol', 'thalach', 'exang','oldpeak']]
y=data['disease']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LogisticRegression()
model.fit(X_train,y_train)
age=st.number_input("enter a numbeter")
cp=st.number_input("enter a cp     ")
trestbps=st.number_input("enter a trestbps")
chol=st.number_input("enter a chol")
thalach=st.number_input("enter a thalach")
exang=st.number_input("enter a exang")
oldpeak=st.number_input("enter a oldpeak")
bt=st.button("SUBMIT")
if bt:
    predicted=model.predict([[age,cp,trestbps,chol,thalach,exang,oldpeak]])
    st.write("the predicted result ",predicted)