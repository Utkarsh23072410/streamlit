import streamlit as st
import datetime
import pandas as pd
import pickle

st.header("Cars Prediction")

cars_df = pd.read_csv("./cars_data.csv")
st.dataframe(cars_df.head())



Fuel_type = st.selectbox(
    "Which type of fuel you want?",
    ("Petrol","Diesel", "CNG","LPG","Electric")
)
Transmission_type=st.selectbox(
    "Which type of Transmission you want ?",
    ("Mannual","Automatic")
)
Engine=st.slider("Set the Engine power",
                 500,1000,step=100 )
Seat_type=st.selectbox(
    "Enter the number of seats",
    (1,2,3,4)
)

input_dict = {
    "Fuel_type": {"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5,},
    "Seller_type":{"Dealer" : 1,"Individual":2,"Trustmark Dealer":3},
    "Transmission_type": {"Mannual":1,"Automatic":2}
    
}

def model_pred(Fuel_type,Transmission_type,Engine,Seat_type):
    
    
    #loading the model
    with open("car_pred_model",'rb') as file:
        reg_model=pickle.load(file)
        input_features = [[2018.0, 1, 4000, Fuel_type,\
            Transmission_type, 19.70, Engine, 86.30,\
                Seat_type]]
        
        return reg_model.predict(input_features)

if st.button("Predict Price"):
    Fuel_type = input_dict["Fuel_type"][Fuel_type]
    Transmission_type = input_dict["Transmission_type"][Transmission_type]

    price = model_pred(Fuel_type, Transmission_type, Engine, Seat_type)

    st.text(f"The price of the car is {price[0].round(2)} lakhs")
                            