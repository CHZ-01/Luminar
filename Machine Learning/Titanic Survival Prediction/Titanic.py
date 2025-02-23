import streamlit as st
import numpy as np
import pickle 

with open("Titanic.pkl","rb") as f:
    dit = pickle.load(f)


st.title("Titanic Survival Prediction")

Age = st.number_input("Enter Age:",0,80)
Sex = st.selectbox("Enter Sex:",["Male", "Female"])
Pclass = st.number_input("Enter Passenger Class:",1,3)
SibSp =	st.number_input("Enter Number of Siblings or Spouse:",0,8)
Parch = st.number_input("Enter Number of Parents or Children:",0,6)
Fare =	st.number_input("Enter Fare:",0,300)
Embarked = st.selectbox("Enter Embarked:",["S","C","Q"])
btn = st.button("Check")

# x_test = [Pclass,Age,SibSp,Parch,Fare,Embarked,Sex]

if btn:
    ohe_embarked = np.array(dit["oh_embarked"].transform([[Embarked]]))
    ohe_sex = np.array(dit["oh_sex"].transform([[Sex.lower()]]))
    
    features = np.array([[Pclass,Age,SibSp,Parch,Fare]])

    x_test = np.hstack((features,ohe_embarked,ohe_sex))
    x_scaled = dit["scaler"].transform(x_test)
    y_pred = dit["model"].predict(x_scaled)
    
    if y_pred == 1:
        st.text("The passenger survived the Titanic disaster.")
    else:
        st.text("The passenger did not survive the Titanic disaster.")