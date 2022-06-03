import streamlit as st
st.write("Hello!")

categories = ['a', 'b', 'c']
st.multiselect("Pick a category", categories)
