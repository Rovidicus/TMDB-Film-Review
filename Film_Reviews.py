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
with open('config/filepaths.json') as f:
    FPATHS = json.load(f)
st.title("Predicting Yelp Review Ratings")

## Loading our training and test data
@st.cache_data
def load_Xy_data(joblib_fpath):
    return joblib.load(joblib_fpath)
# Load training data from FPATHS
train_data_fpath  = FPATHS['data']['ml']['train']
X_train, y_train = load_Xy_data(train_data_fpath)
# Load test data from FPATHS
test_data_fpath  = FPATHS['data']['ml']['test']
X_test, y_test = load_Xy_data(test_data_fpath)

from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
def classification_metrics_streamlit(y_true, y_pred, label='',
                           figsize=(8,4),
                           normalize='true', cmap='Blues',
                           colorbar=False,values_format=".2f",
                                    class_names=None):
    """Modified version of classification metrics function from Intro to Machine Learning.
    Updates:
    - Reversed raw counts confusion matrix cmap  (so darker==more).
    - Added arg for normalized confusion matrix values_format
    """
    # Get the classification report
    report = classification_report(y_true, y_pred,target_names=class_names)
    
    ## Save header and report
    header = "-"*70
    final_report = "\n".join([header,f" Classification Metrics: {label}", header,report,"\n"])
        
    ## CONFUSION MATRICES SUBPLOTS
    fig, axes = plt.subplots(ncols=2, figsize=figsize)
    
    # Create a confusion matrix  of raw counts (left subplot)
    ConfusionMatrixDisplay.from_predictions(y_true, y_pred,
                                            normalize=None, 
                                            cmap='gist_gray_r',# Updated cmap
                                            display_labels = class_names, # Added display labels
                                            values_format="d", 
                                            colorbar=colorbar,
                                            ax = axes[0]);
    axes[0].set_title("Raw Counts")
    
    # Create a confusion matrix with the data with normalize argument 
    ConfusionMatrixDisplay.from_predictions(y_true, y_pred,
                                            normalize=normalize,
                                            cmap=cmap, 
                                            values_format=values_format, #New arg
                                            display_labels = class_names, # Added display labels
                                            colorbar=colorbar,
                                            ax = axes[1]);
    axes[1].set_title("Normalized Confusion Matrix")
    
    # Adjust layout and show figure
    fig.tight_layout()
    return final_report, fig


# Get text to predict from the text input box
X_to_pred = st.text_input("### Enter text to predict here:", 
                          value="I loved the characters and action! Great film.")

# Loading the ML model
@st.cache_resource
def load_ml_model(fpath):
    loaded_model = joblib.load(fpath)
    return loaded_model
# Load model from FPATHS
model_fpath = FPATHS['models']['rf']
clf_pipe = load_ml_model(model_fpath)

import joblib
# load target lookup dict
@st.cache_data
def load_lookup(fpath=FPATHS['data']['ml']['target_lookup']):
    return joblib.load(fpath)
@st.cache_resource
def load_encoder(fpath=FPATHS['data']['ml']['label_encoder'] ):
    return joblib.load(fpath)

# Load the target lookup dictionary
target_lookup = load_lookup()
# Load the encoder
encoder = load_encoder()
# Update the function to decode the prediction
def make_prediction(X_to_pred, clf_pipe=clf_pipe, lookup_dict= target_lookup):
    # Get Prediction
    pred_class = clf_pipe.predict([X_to_pred])[0]
    # Decode label
    pred_class = lookup_dict[pred_class]
    return pred_class


from lime.lime_text import LimeTextExplainer
@st.cache_resource
def get_explainer(class_names = None):
    lime_explainer = LimeTextExplainer(class_names=class_names)
    return lime_explainer
    
def explain_instance(explainer, X_to_pred, predict_func):
    explanation = explainer.explain_instance(X_to_pred, predict_func)
    return explanation.as_html(predict_proba=False)
# Create the lime explainer
explainer = get_explainer(class_names = encoder.classes_)



# Trigger prediction and explanation with a button
if st.button("Get prediction."):
    pred_class_name = make_prediction(X_to_pred)
    st.markdown(f"##### Predicted category:  {pred_class_name}")
    # Get the Explanation as html and display using the .html component.
    html_explanation = explain_instance(explainer, X_to_pred, clf_pipe.predict_proba)
    components.html(html_explanation, height=400)
else: 
    st.empty()

​## To place the 3 checkboxes side-by-side
col1,col2,col3 = st.columns(3)
show_train = col1.checkbox("Show training data.", value=True)
show_test = col2.checkbox("Show test data.", value=True)
show_model_params =col3.checkbox("Show model params.", value=False)
if st.button("Show model evaluation."):
    if show_train == True:
        # Display training data results
        y_pred_train = clf_pipe.predict(X_train)
        report_str, conf_mat = classification_metrics_streamlit(y_train, y_pred_train, label='Training Data')
        st.text(report_str)
        st.pyplot(conf_mat)
        st.text("\n\n")
    if show_test == True: 
        # Display the trainin data resultsg
        y_pred_test = clf_pipe.predict(X_test)
        report_str, conf_mat = classification_metrics_streamlit(y_test, y_pred_test, cmap='Reds',label='Test Data')
        st.text(report_str)
        st.pyplot(conf_mat)
        st.text("\n\n")
        
    if show_model_params:
        # Display model params
        st.markdown("####  Model Parameters:")
        st.write(clf_pipe.get_params())
else:
    st.empty()
