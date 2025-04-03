import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide")

# Apply background image using CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load trained models
diabetes_model = pickle.load(open(r'diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open(r'heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open(r'parkinsons_model.sav', 'rb'))
# lung_cancer_model = pickle.load(open(r'lungs_disease_model.sav', 'rb'))
# thyroid_model = pickle.load(open(r'Thyroid_model.sav', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        "Disease Outbreak Prediction System",
        [
            "Diabetes Prediction"
        ],
        menu_icon="hospital-fill",
        icons=["activity"],
        default_index=0,
    )

# Function for making predictions
def predict_disease(model, labels):
    """Handles user input and makes predictions."""
    user_input = []
    col1, col2, col3 = st.columns(3)
    
    for i, label in enumerate(labels):
        with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
            value = st.text_input(label, "")
            user_input.append(value)
    
    if st.button("Get Prediction Result"):
        if not all(user_input):
            st.warning("Please fill in all fields before proceeding.")
        else:
            try:
                user_input = list(map(lambda x: float(x) if x else 0.0, user_input))
                prediction = model.predict([user_input])
                result = "The person has the disease." if prediction[0] == 1 else "The person does not have the disease."
                st.success(result)
            except ValueError:
                st.error("Please enter valid numerical values.")

# **Diabetes Prediction**
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction Using ML")
    diabetes_labels = [
        "Number of Pregnancies", "Glucose Level", "Blood Pressure", 
        "Skin Thickness", "Insulin Level", "BMI", 
        "Diabetes Pedigree Function", "Age"
    ]
    predict_disease(diabetes_model, diabetes_labels)

# # **Heart Disease Prediction**
# if selected == "Heart Disease Prediction":
#     st.title("Heart Disease Prediction Using ML")
#     heart_labels = [
#         "Age", "Sex (0 = Female, 1 = Male)", "Chest Pain Type", 
#         "Resting Blood Pressure", "Cholesterol Level", "Fasting Blood Sugar (1=True, 0=False)", 
#         "Resting ECG Results", "Max Heart Rate Achieved", "Exercise-Induced Angina (1=Yes, 0=No)", 
#         "ST Depression Induced by Exercise", "Slope of Peak Exercise ST Segment", 
#         "Major Vessels Colored by Fluoroscopy", "Thalassemia (0-3)"
#     ]
#     predict_disease(heart_disease_model, heart_labels)

# # **Parkinson’s Prediction**
# if selected == "Parkinsons Prediction":
#     st.title("Parkinsons Prediction Using ML")
#     parkinsons_labels = [
#         "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", 
#         "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", 
#         "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", 
#         "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", 
#         "MDVP:APQ", "Shimmer:DDA", "NHR", 
#         "HNR", "RPDE", "DFA", 
#         "spread1", "spread2", "D2", "PPE"
#     ]
#     predict_disease(parkinsons_model, parkinsons_labels)

# # # **Lung Cancer Prediction**
# if selected == "Lung Cancer Prediction":
#     st.title("Lung Cancer Prediction Using ML")
    
#     lung_cancer_labels = [
#         "Gender (1 = Male; 0 = Female)", "Age", "Smoking ",
#         "Yellow Fingers", "Anxiety",
#         "Peer Pressure", "Chronic Disease",
#         "Fatigue", "Allergy",
#         "Wheezing", "Alcohol Consuming",
#         "Coughing ", "Shortness Of Breath",
#         "Swallowing Difficulty", "Chest Pain"
#     ]
    
#     predict_disease(lung_cancer_model, lung_cancer_labels)


# # **Thyroid Disease Prediction**
# if selected == "Thyroid Disease Prediction":
#     st.title("Hypo-Thyroid Prediction Using ML")
#     thyroid_labels = [
#         "Age", "Sex (1=Male, 0=Female)", "On Thyroxine (1=Yes, 0=No)", 
#         "TSH Level", "T3 Measured (1=Yes, 0=No)", "T3 Level", 
#         "TT4 Level"
#     ]
#     predict_disease(thyroid_model, thyroid_labels)

