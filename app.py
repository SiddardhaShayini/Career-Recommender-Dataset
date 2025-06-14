import streamlit as st
import pandas as pd
import numpy as np
from components.chat_interface import ChatInterface
from utils.career_recommender import CareerRecommender
from data.interests_mapping import INTERESTS_LIST, INTEREST_KEYWORDS
import os

with open("requirements.txt", "r") as file:
    print("🚨 REQUIREMENTS.TXT CONTENT 🚨")
    print(file.read())


# Page configuration
st.set_page_config(
    page_title="AI Virtual Career Counsellor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

def main():
    # Header
    st.title("🎯 AI Virtual Career Counsellor")
    st.markdown("### Discover your ideal career path based on your interests and skills!")
    
    # Sidebar for user profile
    with st.sidebar:
        st.header("📋 Your Profile")
        
        # Method selection
        input_method = st.radio(
            "How would you like to provide your interests?",
            ["💬 Chat with AI", "✅ Select from List", "📝 Both Methods"]
        )
        
        if input_method in ["✅ Select from List", "📝 Both Methods"]:
            st.subheader("Select Your Interests")
            
            # Clear button
            if st.button("🗑️ Clear All Selections", key="clear_interests"):
                for i in range(len(INTERESTS_LIST)):
                    if f"interest_{i}" in st.session_state:
                        st.session_state[f"interest_{i}"] = False
                st.session_state.user_profile['selected_interests'] = []
                st.rerun()
            
            selected_interests = []
            
            # Create columns for better layout
            cols = st.columns(2)
            for i, interest in enumerate(INTERESTS_LIST):
                with cols[i % 2]:
                    if st.checkbox(interest.replace('_', ' ').title(), key=f"interest_{i}"):
                        selected_interests.append(interest)
            
            st.session_state.user_profile['selected_interests'] = selected_interests
            
            if selected_interests:
                st.success(f"Selected {len(selected_interests)} interests")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if input_method in ["💬 Chat with AI", "📝 Both Methods"]:
            st.subheader("💬 Chat Interface")
            chat_interface = ChatInterface()
            chat_interface.render()
        
        # Display recommendations if available
        if st.session_state.recommendations:
            st.subheader("🎓 Your Personalized Recommendations")
            
            # Course recommendations
            if 'course' in st.session_state.recommendations:
                st.markdown("#### 📚 Recommended Course")
                course = st.session_state.recommendations['course']
                st.info(f"**{course}**")
            
            # Career recommendations
            if 'careers' in st.session_state.recommendations:
                st.markdown("#### 💼 Career Options")
                careers = st.session_state.recommendations['careers']
                if isinstance(careers, list):
                    for i, career in enumerate(careers, 1):
                        st.success(f"{i}. {career}")
                else:
                    st.success(careers)
    
    with col2:
        st.subheader("📊 Profile Summary")
        
        # Display current user profile
        if st.session_state.user_profile:
            if 'selected_interests' in st.session_state.user_profile:
                interests = st.session_state.user_profile['selected_interests']
                if interests:
                    st.write("**Selected Interests:**")
                    for interest in interests:
                        st.markdown(f"• {interest.replace('_', ' ').title()}")
            
            if 'chat_keywords' in st.session_state.user_profile:
                keywords = st.session_state.user_profile['chat_keywords']
                if keywords:
                    st.write("**Keywords from Chat:**")
                    for keyword in keywords:
                        st.markdown(f"• {keyword}")
        else:
            st.info("Start chatting or select interests to build your profile!")
        
        # Action buttons
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🔍 Get Career Recommendations", type="primary"):
                with st.spinner("Analyzing your profile..."):
                    try:
                        recommender = CareerRecommender()
                        recommendations = recommender.get_recommendations(st.session_state.user_profile)
                        st.session_state.recommendations = recommendations
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error getting recommendations: {str(e)}")
        
        with col_btn2:
            if st.button("🗑️ Clear Profile", type="secondary"):
                # Clear user profile
                st.session_state.user_profile = {}
                st.session_state.recommendations = None
                # Clear interest checkboxes
                for i in range(len(INTERESTS_LIST)):
                    if f"interest_{i}" in st.session_state:
                        st.session_state[f"interest_{i}"] = False
                st.success("Profile cleared!")
                st.rerun()
        
        # Clear chat button
        if st.button("🧹 Clear Chat History"):
            st.session_state.messages = []
            st.success("Chat history cleared!")
            st.rerun()
        
        # Sample interaction examples
        st.subheader("💡 Try These Examples")
        
        # Interest-based examples
        st.write("**Tell me about your interests:**")
        interest_examples = [
            "I love coding and solving problems",
            "I'm interested in art and design",
            "I enjoy working with numbers and data"
        ]
        
        for example in interest_examples:
            if st.button(f"💬 \"{example}\"", key=f"interest_{hash(example)}"):
                st.session_state.messages.append({"role": "user", "content": example})
                st.rerun()
        
        # Q&A examples
        st.write("**Ask career questions:**")
        qa_examples = [
            "What's the salary for a software developer?",
            "What education do I need to become a nurse?",
            "Compare marketing manager vs financial analyst",
            "What are the trends in technology industry?"
        ]
        
        for example in qa_examples:
            if st.button(f"❓ \"{example}\"", key=f"qa_{hash(example)}"):
                st.session_state.messages.append({"role": "user", "content": example})
                st.rerun()

if __name__ == "__main__":
    main()
