# AI Virtual Career Counsellor

## Overview

This is an AI-powered career counselling application built with Streamlit that helps users discover personalized career paths and course recommendations based on their interests and skills. The system uses machine learning models to analyze user input and provide tailored suggestions through both an interactive chat interface and a checklist-based approach.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Frontend**: Streamlit web interface with chat functionality and sidebar controls
- **Backend**: Python-based recommendation engine using machine learning models
- **Models**: Pre-trained Random Forest and Neural Network models for course and career prediction
- **Data Processing**: Natural Language Processing pipeline using NLTK for text analysis
- **Deployment**: Configured for Replit's autoscale deployment target

## Key Components

### 1. Main Application (`app.py`)
- Entry point of the application
- Handles page configuration and session state management
- Manages user profile data and recommendation display
- Provides dual input methods: chat interface and interest selection

### 2. Chat Interface (`components/chat_interface.py`)
- Interactive conversational UI for gathering user interests
- Real-time keyword extraction from user messages
- Contextual response generation based on extracted interests
- Session-based chat history management

### 3. Career Recommender (`utils/career_recommender.py`)
- Core recommendation engine
- Creates feature vectors from user profiles
- Interfaces with machine learning models for predictions
- Provides fallback recommendations when models are unavailable

### 4. Text Processor (`utils/text_processor.py`)
- NLTK-based natural language processing
- Text preprocessing with lemmatization and stopword removal
- Keyword extraction mapping user input to predefined interests
- Caches NLTK data downloads for performance

### 5. Model Loader (`models/model_loader.py`)
- Manages loading of pre-trained ML models
- Handles Random Forest course recommendation model
- Manages TensorFlow/Keras career prediction neural network
- Implements caching for model loading optimization

### 6. Interest Mapping (`data/interests_mapping.py`)
- Defines 59 predefined interest categories
- Maps natural language keywords to structured interests
- Enables both checklist selection and NLP-based interest detection

## Data Flow

1. **User Input**: Users provide interests through chat or checklist selection
2. **Text Processing**: Chat input is processed through NLTK pipeline for keyword extraction
3. **Feature Creation**: User profile is converted to feature vector based on interest mapping
4. **Model Prediction**: Feature vector is fed to ML models for course and career predictions
5. **Recommendation Display**: Results are presented through the Streamlit interface

## External Dependencies

### Core Libraries
- **Streamlit**: Web application framework for user interface
- **NLTK**: Natural language processing for text analysis
- **Scikit-learn**: Machine learning model support and utilities
- **TensorFlow**: Deep learning framework for neural network models
- **Pandas/NumPy**: Data manipulation and numerical computing

### Model Files
- `random_forest_courses_model_1749886366074.pkl`: Course recommendation model
- `courses_label_encoder_1749886366076.pkl`: Label encoder for course categories
- `career_model_1749886366074.h5`: Neural network for career predictions
- `cleaned_dataset_1749886376399.csv`: Training dataset with interest-career mappings

## Deployment Strategy

The application is configured for deployment on Replit's platform:

- **Target**: Autoscale deployment for automatic scaling
- **Runtime**: Python 3.11 with Nix package management
- **Port**: Configured to run on port 5000
- **Entry Point**: `streamlit run app.py --server.port 5000`
- **Workflow**: Parallel execution with shell command tasks

The deployment configuration ensures the application can handle variable user loads while maintaining consistent performance.

## Recent Changes

- June 14, 2025: Enhanced with comprehensive career knowledge base and intelligent Q&A system
- Added advanced NLP features including sentiment analysis, named entity recognition, and career term extraction
- Integrated web scraping capabilities for real-time career information
- Implemented rule-based career recommendations as fallback for ML models
- Added clear button for interest selections and improved user interface

## Changelog

- June 14, 2025. Initial setup with ML models and basic chat interface
- June 14, 2025. Enhanced with intelligent career Q&A system and comprehensive knowledge base

## User Preferences

- Preferred communication style: Simple, everyday language
- Wants free and open-source solutions only for external services
- Prefers comprehensive career information with real salary data and job market insights
- Values both chat interface and checklist selection methods for input