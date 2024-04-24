import streamlit as st
# Create multiple pages from apps in pages folder
st.set_page_config()

st.title("Film Critique ")
st.subheader("by Luke Hobbs")

st.markdown("This is my analysis of film reviews from a natural language processing perspective. The objective is to predict from a given text if a review is positive or negative toward a film.")

st.markdown("People are passionate about their entertainment. Gleaming a dataset from TMDB chalk full of strong words and bluster helps machine learning pick up sentiment from key word choices and associate positive or negative feelings therewith. For our purpose, we've selected reviews that were very positive or very negative to analyze.")

st.header("Contact Information")
contact_info="""
- [Email](rovidicus@hotmail.com)
- [GitHub Profile](https://github.com/Rovidicus?tab=repositories")
- [LinkedIn](www.linkedin.com/in/lukenhobbs)
"""
st.markdown(contact_info)

