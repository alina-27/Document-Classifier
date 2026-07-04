import streamlit as st

st.title("📄 Document Classifier")

st.write("Welcome to my first AI/ML project!")

text = st.text_area("Enter some text")

if st.button("Classify"):
    st.success("Prediction will appear here.")