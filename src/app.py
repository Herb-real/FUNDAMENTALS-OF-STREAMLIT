
import streamlit as st
import pandas as pd
import numpy as np
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
_file_ = "C:\Users\LPM\Desktop\FUNDAMENTALS OF STREAMLIT\src"
DIRPATH = os.path.dirname(os.path.realpath(_file_))  
ml_core_fp = os.path.join(DIRPATH, "assets", "ml", "ml_components.pkl")

## Execution
ml_components_dict = load_ml_components(fp=ml_core_fp)

labels = ml_components_dict['labels']
idx_to_labels = {i: l for (i, l) in enumerate(labels)}

end2end_pipeline = ml_components_dict['pipeline']


print(f"\n[Info] Predictable labels: {labels}")
print(f"\n[Info] Indexes to labels: {idx_to_labels}")

print(f"\n[Info] ML components loaded: {list(ml_components_dict.keys())}")

# image
st.image("https://www.marktechpost.com/wp-content/uploads/2023/02/stock-market-chart-virtual-screen-with-woman-s-hand-digital-remix-scaled.jpg")

# interface
with st.sidebar:
    st.markdown("# Hi")
    st.markdown("# Welcome. This app is on time series forecasting")
    
st.title ('Sales Prediction in Favorita Stores')

st.subheader ('Using Time Series Forecasting') 

# Add some text
st.write("""Welcome to Favorita Corporation, an Ecuadorian company which engages in the development and investment of commercial, industrial, and real estate ventures. Its subsidiaries operate in six countries within the region, namely Panama, Paraguay, Peru, Colombia, Costa Rica, and Chile. The company is committed to delivering top-notch products, services, and experiences in a manner that is both efficient and environmentally responsible, aiming to enhance the overall quality of life.


         
         Please ENTER the relevant data and CLICK Predict.
         
         """ )

     
with st.form(key="information", clear_on_submit=True):
    
    # Inputs
    store_nbr = st.slider("Enter store nbr",0,54)
    products = st.selectbox(" Family", ['OTHERS', 'CLEANING', 'FOODS', 'STATIONERY', 'GROCERY', 'HARDWARE',
        'HOME', 'CLOTHING'])
    onpromotion = st.number_input("Discount Amt On Promotion_Expressed in Percentage %",step=1)
    state = st.selectbox("State", ['Choose a State', 'Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura',
        'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
        'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
        'El Oro', 'Esmeraldas', 'Manabi'])

    store_type = st.selectbox("Store Type",['Choose Store Type', 'D', 'C', 'B', 'E', 'A'])
    Cluster = st.number_input("Cluster",step=1)
    dcoilwtico = st.number_input("DCOILWTICO",step=1)
    year = st.number_input("Year to Predict",step=1)

    month = st.slider("Month",1,12)
    day = st.slider("Day",1,31)
    dayofweek = st.number_input("Day of Week,0=Sunday and 6=Satruday",step=1)


    # prediction executed
    if st.form_submit_button("Predict"):
        try:
            # Dataframe creation
            df = pd.DataFrame(
                {
                "store_nbr":[store_nbr],  "products":[products], "onpromotion":[onpromotion], "state": [state], "store_type": [store_type],
                "Cluster": [Cluster], "dcoilwtico":[dcoilwtico], "year":[year], "month":[month], "day":[day], "dayofweek":[dayofweek],
            
                }   
                    )
            print(f"[Info] Input data as dataframe:\n{df.to_markdown()}")
            
            df.columns = num_cols+cat_cols
            df = df[num_cols+cat_cols] #reorder the dataframe
    
            # ML part
            output = end2end_pipeline.predict_proba(df)
    
            ## store confidence score/ probability for the predicted class
            df['confidence score'] = output.max(axis=-1)
    
            ## get index of the predicted class
            predicted_idx = output.argmax(axis=-1)
    
            # store index then replace by the matching label
            df['predicted label'] = predicted_idx
            df['predicted label'] = df['predicted label'].replace(idx_to_labels) 
   
    
            st.text(f"The Predicted Sales: '{''}'.")
        except:
            st.error(f"Something went wrong during prediction.") 