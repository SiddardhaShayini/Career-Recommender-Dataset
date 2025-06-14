import os
import numpy as np
import pandas as pd
from utils.text_processor import TextProcessor
from models.model_loader import ModelLoader
import streamlit as st

class CareerRecommender:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.model_loader = ModelLoader()
        
    def get_recommendations(self, user_profile):
        """Get course and career recommendations based on user profile"""
        try:
            # Create feature vector from user profile
            feature_vector = self._create_feature_vector(user_profile)
            
            if sum(feature_vector) == 0:
                return {
                    'course': 'Please provide more information about your interests to get personalized recommendations.',
                    'careers': ['Share your skills and hobbies to discover suitable career paths!']
                }
            
            # Get course recommendation
            course_recommendation = self._get_course_recommendation(feature_vector)
            
            # Get career recommendations
            career_recommendations = self._get_career_recommendations(feature_vector)
            
            return {
                'course': course_recommendation,
                'careers': career_recommendations
            }
            
        except Exception as e:
            st.error(f"Error in recommendation system: {str(e)}")
            return self._get_fallback_recommendations(user_profile)
    
    def _create_feature_vector(self, user_profile):
        """Create feature vector from user profile data"""
        from data.interests_mapping import INTERESTS_LIST
        
        feature_vector = [0] * len(INTERESTS_LIST)
        
        # Process selected interests
        if 'selected_interests' in user_profile:
            for interest in user_profile['selected_interests']:
                try:
                    idx = INTERESTS_LIST.index(interest)
                    feature_vector[idx] = 1
                except ValueError:
                    continue
        
        # Process chat keywords
        if 'chat_keywords' in user_profile:
            for keyword in user_profile['chat_keywords']:
                try:
                    if keyword in INTERESTS_LIST:
                        idx = INTERESTS_LIST.index(keyword)
                        feature_vector[idx] = 1
                except ValueError:
                    continue
        
        return feature_vector
    
    def _get_course_recommendation(self, feature_vector):
        """Get course recommendation using the trained model"""
        try:
            # Load models
            course_model = self.model_loader.load_course_model()
            course_encoder = self.model_loader.load_course_encoder()
            
            if course_model is None or course_encoder is None:
                return self._get_fallback_course_recommendation(feature_vector)
            
            # Make prediction
            prediction = course_model.predict([feature_vector])[0]
            course_name = course_encoder.inverse_transform([prediction])[0]
            
            return course_name
            
        except Exception as e:
            return self._get_fallback_course_recommendation(feature_vector)
    
    def _get_career_recommendations(self, feature_vector):
        """Get career recommendations using the trained model"""
        try:
            # Load models
            career_model = self.model_loader.load_career_model()
            career_encoder = self.model_loader.load_career_encoder()
            
            if career_model is None or career_encoder is None:
                return self._get_fallback_career_recommendations(feature_vector)
            
            # Make prediction
            prediction = career_model.predict([feature_vector])[0]
            
            # Convert binary predictions to career names
            threshold = 0.5
            predicted_careers = []
            
            for i, prob in enumerate(prediction):
                if prob > threshold:
                    career_labels = career_encoder.classes_
                    if i < len(career_labels):
                        predicted_careers.append(career_labels[i])
            
            if not predicted_careers:
                # If no careers above threshold, take top 3
                top_indices = np.argsort(prediction)[-3:][::-1]
                predicted_careers = [career_encoder.classes_[i] for i in top_indices if i < len(career_encoder.classes_)]
            
            return predicted_careers[:5]  # Return top 5 careers
            
        except Exception as e:
            return self._get_fallback_career_recommendations(feature_vector)
    
    def _get_fallback_course_recommendation(self, feature_vector):
        """Provide rule-based course recommendations as fallback"""
        from data.interests_mapping import INTERESTS_LIST
        
        active_interests = [INTERESTS_LIST[i] for i, val in enumerate(feature_vector) if val == 1 and i < len(INTERESTS_LIST)]
        
        # Rule-based course mapping
        if any(interest in ['Coding', 'Computer_Parts', 'Mathematics'] for interest in active_interests):
            return "B.Tech Computer Science Engineering"
        elif any(interest in ['Drawing', 'Designing', 'Crafting'] for interest in active_interests):
            return "BFD- Bachelor of Fashion Designing"
        elif any(interest in ['Economics', 'Accounting', 'Bussiness_Education'] for interest in active_interests):
            return "BBA- Bachelor of Business Administration"
        elif any(interest in ['Content_Writing', 'Literature', 'Reading', 'Debating'] for interest in active_interests):
            return "BJMC- Bachelor of Journalism and Mass Communication"
        elif any(interest in ['Teaching', 'Psychology', 'Sociology'] for interest in active_interests):
            return "B.Ed- Bachelor of Education"
        else:
            return "Liberal Arts Program - Explore your interests across multiple disciplines"
    
    def _get_fallback_career_recommendations(self, feature_vector):
        """Provide rule-based career recommendations as fallback"""
        from data.interests_mapping import INTERESTS_LIST
        
        active_interests = [INTERESTS_LIST[i] for i, val in enumerate(feature_vector) if val == 1 and i < len(INTERESTS_LIST)]
        
        careers = []
        
        # Rule-based career mapping
        if any(interest in ['Coding', 'Computer_Parts'] for interest in active_interests):
            careers.extend(["Software Developer", "Data Scientist", "Systems Analyst"])
        if any(interest in ['Drawing', 'Designing'] for interest in active_interests):
            careers.extend(["Graphic Designer", "UI/UX Designer", "Art Director"])
        if any(interest in ['Economics', 'Accounting'] for interest in active_interests):
            careers.extend(["Financial Analyst", "Accountant", "Business Consultant"])
        if any(interest in ['Content_Writing', 'Literature'] for interest in active_interests):
            careers.extend(["Content Writer", "Journalist", "Editor"])
        if any(interest in ['Teaching', 'Psychology'] for interest in active_interests):
            careers.extend(["Teacher", "Counselor", "Training Specialist"])
        
        if not careers:
            careers = ["Career Counselor", "Project Manager", "Research Analyst", "Consultant"]
        
        return careers[:5]
    
    def _get_fallback_recommendations(self, user_profile):
        """Provide basic recommendations when models fail"""
        return {
            'course': 'Liberal Arts - A flexible program to explore various fields',
            'careers': [
                'Career Counselor - Help others find their path',
                'Project Manager - Coordinate diverse projects',
                'Research Analyst - Investigate various topics',
                'Consultant - Provide expertise across fields'
            ]
        }
