import streamlit as st

st.title("📄 Document Classifier")

st.write("Welcome to my Document Classifier!")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["txt", "pdf"]
)

if uploaded_file:
    st.success("File uploaded successfully!")
    st.write(uploaded_file.name)