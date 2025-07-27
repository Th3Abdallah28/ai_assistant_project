
import streamlit as st
from assistant import run_query

st.set_page_config(page_title="AI Assistant")
st.title("🤖 AI Personal Assistant")

query = st.text_input("What would you like to ask?")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        response = run_query(query)
        st.success(response)

