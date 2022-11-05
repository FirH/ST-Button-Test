import streamlit as st

col1, col2 = st.columns((1,5))
with col1 :
    avs = st.button('Test')
with col2 :
    krs = st.button('Test2')

if(avs) :
    st.write('Mampus')
if(krs) :
    st.write('Haha')
