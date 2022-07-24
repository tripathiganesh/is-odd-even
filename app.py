import streamlit as st

st.write("""
# Number identifier App

This app identifies the entered number is odd or even
""")
#Get Input

st.header('User Input Parameters')
num = st.number_input('Enter the number')
st.subheader('RESULT')
if (num % 2) == 0:
    st.write('The entered number is EVEN')
else:
    st.write('The entered number is ODD')
