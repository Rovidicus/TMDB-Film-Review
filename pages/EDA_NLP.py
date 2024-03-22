import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import json
from wordcloud import WordCloud
from nltk import casual_tokenize
# Changing the Layout
st.set_page_config( layout="wide")

with open('config/filepaths.json') as f:
    FPATHS = json.load(f)

st.title("Exploratory Data Analysis of TMDB Reviews")


@st.cache_data
def load_data(fpath):
    return joblib.load(fpath)

df = load_data(FPATHS['data']['processed'])
df.head(2)

# select which version of positive wordclouds
wc_choice_high = st.radio("Select Positive WordCloud Text: ", ["Tokens",'Lemmas'], index=0, horizontal=True)
wc_choice_high

if wc_choice_high=='Lemmas':
    fpath_wc = FPATHS['eda']['lemmas-high']
else:
    fpath_wc = FPATHS['eda']['tokens-high']
st.image(fpath_wc)

# select which version of negative wordclouds
wc_choice_low = st.radio("Select Negative WordCloud Text: ", ["Tokens",'Lemmas'], index=0, horizontal=True)
wc_choice_low

if wc_choice_low=='Lemmas':
    fpath_wc = FPATHS['eda']['lemmas-low']
else:
    fpath_wc = FPATHS['eda']['tokens-low']
st.image(fpath_wc)

