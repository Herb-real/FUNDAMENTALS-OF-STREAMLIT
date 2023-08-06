
import streamlit as st
import pandas as pd
import pickle
import joblib, os

# Useful functions
def load_ml_components(fp):
    "Load the ml components to re-use in app"
    with open(fp, "rb") as f:
        object = pickle.load(f)
        return object

# Setup
## Variables and constants
#_file_ = "c:\Users\LPM\Desktop\FUNDAMENTALS OF STREAMLIT\.venv"
#DIRPATH = os.path.dirname(os.path.realpath(_file_))
#ml_core_fp = os.path.join(DIRPATH, "assets", "ml", "ml_components.pkl")

## Execution
#ml_components_dict = load_ml_components(fp=ml_core_fp)

#labels = ml_components_dict['labels']
#idx_to_labels = {i: l for (i, l) in enumerate(labels)}

#end2end_pipeline = ml_components_dict['pipeline']


#print(f"\n[Info] Predictable labels: {labels}")
#print(f"\n[Info] Indexes to labels: {idx_to_labels}")

#print(f"\n[Info] ML components loaded: {list(ml_components_dict.keys())}")

# interface
st.write (
    """# My interface

This is my interface using Streamlit.  
     
""")
# Input
sepal_height = st.number_input("Enter sepal height")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")

# prediction executed
if st.button("Predict"):
    # Dataframe creation
    df = pd.DataFrame(
        {
         "sepal_height (cm)":[sepal_height],  "sepal_width (cm)":[sepal_width], 
         "petal_height (cm)":[petal_height], "petal_width (cm)":[petal_width], 
            
        }   
    )
    print(f"[Info] Input data as dataframe:\n{df.to_markdown()}") 
    # df.columns = num_cols+cat_cols
    # df = df[num_cols+cat_cols] #reorder the dataframe
    
    # ML part
    #output = end2end_pipeline.predict_proba(df)
    
    ## store confidence score/ probability for the predicted class
    #df['confidence score'] = output.max(axis=-1)
    
    ## get index of the predicted class
    #predicted_idx = output.argmax(axis=-1)
    
    # store index then replace by the matching label
    #df['predicted label'] = predicted_idx
    #df['predicted label'] = df['predicted label'].replace(idx_to_labels)
    
    
    st.text(f"The iris has been classified as : '{''}'.")