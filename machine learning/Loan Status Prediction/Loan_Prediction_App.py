import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time

# Load the Pickled Model
with open("Loan_Prediction_Model.pkl","rb") as f:
    dit = pickle.load(f)

# Header
st.set_page_config(page_title="Loan Prediction",page_icon=r"img\Page_Icon.png",layout="wide")

# CSS
with open(r"css\app_style.css") as css:
    st.markdown(f"<style>{css.read()}</style>",unsafe_allow_html=True)

# Title
st.image(r"img\Title.png")

# Page Select Session
if "select" not in st.session_state:
    st.session_state.select = "Home Page"

# Image Slideshow
def image_slideshow():
    image_paths = ["img/Image_1.png","img/Image_2.png","img/Image_3.png","img/Image_4.png","img/Image_5.png"]

    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.update_time = time.time()

    if time.time() - st.session_state.update_time > 2:
        st.session_state.index = (st.session_state.index + 1) % len(image_paths)
        st.session_state.update_time = time.time()
        
    b1,img = st.columns([0.2,2])
    img.image(image_paths[st.session_state.index],use_container_width=True)

# Page Class
class Pages:

    # Home
    def home_page(self):    

        intro.title("Welcome") 
        intro.write("to the Loan Status Prediction App! Wondering if your loan will get approved? Our smart prediction system analyzes key factors like loan amount, loan term, and income to assess your eligibility instantly!")
        intro.write("✔ Check approval chances in seconds")
        intro.write("✔ Avoid unnecessary rejections")
        intro.write("✔ Apply with confidence")
        
        b1,btn,b2 = st.columns([1,5,1],vertical_alignment="top")
        # Start Button
        start = btn.button("Get Started",key="start")

        if start:
            st.session_state.select = "First Page"
            st.rerun()

    # First Page
    def first_page(self): 

        st.session_state.Name = intro.text_input("Name:")

        Gender = intro.selectbox("Gender:",["Male","Female"])
        st.session_state.Gender = dit["label"]["Gender"].transform([Gender])[0]

        Married = intro.selectbox("Married:",["Yes","No"])
        st.session_state.Married = dit["label"]["Married"].transform([Married])[0]

        Education = intro.selectbox("Education:",["Graduate","Not Graduate"])
        st.session_state.Education = dit["education"].transform([[Education]])[0,0]

        b1,btn1,btn2,err,b2 = st.columns([1,1.5,1.5,2,1],vertical_alignment="top")
        
        # Back Button
        first_back = btn1.button("Back",key="first_back") 
        # Next Button
        first_next = btn2.button("Next",key="first_next") 

        if first_next:
            if st.session_state.Name == "":
                err.error("Enter Name")
            else:
                st.session_state.select = "Second Page"
                st.rerun()
        elif first_back:
            st.session_state.select = "Home Page"
            st.rerun()

    # Second Page
    def second_page(self): 

        st.session_state.Loan_Amount = intro.number_input("Loan Amount(in Thousands):",10,150)

        st.session_state.Loan_Amount_Term = intro.number_input("Loan Amount Term(in Months):",12,480)

        Self_Employed = intro.selectbox("Self_Employed:",["Yes","No"])
        st.session_state.Self_Employed = dit["label"]["Self_Employed"].transform([Self_Employed])[0]

        Property_Area = intro.selectbox("Property Area:",["Rural","Semiurban","Urban"])
        st.session_state.Property_Area = dit["property"].transform([[Property_Area]])[0,0]
        
        b1,btn1,btn2,b2 = st.columns([1,1.5,1.5,3],vertical_alignment="top")
        
        # Back Button
        second_back = btn1.button("Back",key="second_back") 
        # Next Button
        second_next = btn2.button("Next",key="second_next")

        if second_next:
            st.session_state.select = "Third Page"
            st.rerun()
        elif second_back:
            st.session_state.select = "First Page"
            st.rerun()

    # Third Page
    def third_page(self):

        st.session_state.Dependents = intro.number_input("Dependents:",0,3)

        st.session_state.Applicant_Income = intro.number_input("Applicant Income:",0,10000)

        st.session_state.CoApplicant_Income = intro.number_input("CoApplicant Income:",0,10000)

        b1,btn1,btn2,b2 = st.columns([1,1.5,1.5,3],vertical_alignment="top")
        
        # Back Button
        third_back = btn1.button("Back",key="third_back") 
        # Final Submit
        check = btn2.button("Check",key="check")

        if check:
            st.session_state.select = "Last Page"
            st.rerun()
        elif third_back:
            st.session_state.select = "Second Page"
            st.rerun()

    # Last Page / Output Page
    def last_page(self):
        cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 'Property_Area']

        arr = np.hstack(([st.session_state.Gender],[st.session_state.Married],[st.session_state.Dependents],st.session_state.Education,[st.session_state.Self_Employed],[st.session_state.Applicant_Income],[st.session_state.CoApplicant_Income],[st.session_state.Loan_Amount],[st.session_state.Loan_Amount_Term],st.session_state.Property_Area)).reshape(1,-1)

        df = pd.DataFrame(arr,columns=cols)

        scaled = dit["scaler"].transform(df)
        prediction = dit["model"].predict(scaled)
        
        intro.title("Loan Status")

        if prediction == 0:
            intro.subheader("Sorry,")
            intro.subheader(st.session_state.Name)
            intro.write("Your loan application has been declined! Based on our analysis, you do not meet the eligibility criteria at this time.")
            intro.write("Feel free to review your details and apply again anytime!")
        else:
            intro.subheader("Congrats,")
            intro.subheader(st.session_state.Name)
            intro.write("Your loan application has been approved! Our analysis confirms that you meet the eligibility criteria.")
            intro.write("You’re all set to proceed with your loan. Best of luck with what’s next!")

        b1,btn,b2 = st.columns([1,5,1],vertical_alignment="top")
        
        # Return Home Button
        home = btn.button("Home",key="home")

        if home:
            st.session_state.select = "Home Page"
            st.rerun()

# Class Object
page = Pages()

# Main Container
main_container = st.container(height=500,border=True)

with main_container:
    
    # Side Columns
    col1,col2 = st.columns([0.9,1])
    
    # Side Containers
    container1 = col1.container()
    container2 = col2.container()

    # Image Slideshow
    with container1: 
        image_slideshow()

   # Page Load
    with container2:
        b1,intro,b2 = st.columns([1,5,1],vertical_alignment="top")
        if st.session_state.select == "Home Page":
            page.home_page()
        elif st.session_state.select == "First Page":
            page.first_page()
        elif st.session_state.select == "Second Page":
            page.second_page()
        elif st.session_state.select == "Third Page":    
            page.third_page()
        elif st.session_state.select == "Last Page":
            page.last_page()