import streamlit as st
import pandas as pd

st.write("""
# Number identifier App

This app identifies the entered number is odd or even
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number = st.number_input("NUMBER",min_value=-99,max_value=9999999999999)
    
    data = {'NUMBER': number           
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

st.write(pd.DataFrame({'Result': ['Even','Odd']}))
st.subheader('RESULT')
num = df.iloc[0][0]
if (num % 2) == 0:
    st.write('The entered number is EVEN')
else:
    st.write('The entered number is ODD')
