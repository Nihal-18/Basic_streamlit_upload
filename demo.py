import streamlit as st

st.title('My First Streamlit app')

s= st.text_input('Enter name')

st.write('Hi  '+s)

s1= st.text_input('How are you '+s+' ?')

st.radio('State your level of happiness', (1,2,3,4,5))
