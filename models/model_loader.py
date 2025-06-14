import os
import pickle
import joblib
import streamlit as st
import numpy as np

# TensorFlow is not available in this deployment, using fallback recommendations
TENSORFLOW_AVAILABLE = False

class ModelLoader:
    def __init__(self):
        self.models_path = "attached_assets"
        
    @st.cache_resource
    def load_course_model(_self):
        """Load the Random Forest course recommendation model"""
        try:
            model_path = os.path.join(_self.models_path, "random_forest_courses_model_1749886366074.pkl")
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    model = pickle.load(f)
                return model
            else:
                st.warning("Course model file not found. Using fallback recommendations.")
                return None
        except Exception as e:
            st.error(f"Error loading course model: {str(e)}")
            return None
    
    @st.cache_resource
    def load_course_encoder(_self):
        """Load the course label encoder"""
        try:
            encoder_path = os.path.join(_self.models_path, "courses_label_encoder_1749886366076.pkl")
            if os.path.exists(encoder_path):
                with open(encoder_path, 'rb') as f:
                    encoder = pickle.load(f)
                return encoder
            else:
                st.warning("Course encoder file not found. Using fallback recommendations.")
                return None
        except Exception as e:
            st.error(f"Error loading course encoder: {str(e)}")
            return None
    
    @st.cache_resource
    def load_career_model(_self):
        """Load the career recommendation neural network model"""
        # TensorFlow model not available in deployment environment
        # Application uses intelligent rule-based recommendations instead
        return None
    
    @st.cache_resource
    def load_career_encoder(_self):
        """Load the career options multilabel binarizer"""
        try:
            encoder_path = os.path.join(_self.models_path, "career_options_mlb_1749886366075.pkl")
            if os.path.exists(encoder_path):
                with open(encoder_path, 'rb') as f:
                    encoder = pickle.load(f)
                return encoder
            else:
                st.warning("Career encoder file not found. Using fallback recommendations.")
                return None
        except Exception as e:
            st.error(f"Error loading career encoder: {str(e)}")
            return None
    
    @st.cache_data
    def load_dataset(_self):
        """Load the cleaned dataset"""
        try:
            dataset_path = os.path.join(_self.models_path, "cleaned_dataset_1749886376399.csv")
            if os.path.exists(dataset_path):
                import pandas as pd
                df = pd.read_csv(dataset_path)
                return df
            else:
                st.warning("Dataset file not found.")
                return None
        except Exception as e:
            st.error(f"Error loading dataset: {str(e)}")
            return None
