import streamlit as st
from utils.text_processor import TextProcessor
from utils.career_recommender import CareerRecommender
from utils.career_qa_system import CareerQASystem

class ChatInterface:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.qa_system = CareerQASystem()
        
    def render(self):
        """Render the chat interface"""
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Process the last message if it hasn't been processed yet
        if (len(st.session_state.messages) > 0 and 
            st.session_state.messages[-1]["role"] == "user" and
            (len(st.session_state.messages) == 1 or 
             st.session_state.messages[-2]["role"] == "user")):
            
            prompt = st.session_state.messages[-1]["content"]
            self._process_user_message(prompt)
        
        # Chat input
        if prompt := st.chat_input("Tell me about your interests, hobbies, and skills..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            self._process_user_message(prompt)
    
    def _process_user_message(self, prompt):
        """Process user message and generate response"""
        # Enhanced NLP processing
        keywords = self.text_processor.extract_keywords(prompt)
        question_type = self.text_processor.get_question_type(prompt)
        sentiment = self.text_processor.get_text_sentiment(prompt)
        career_terms = self.text_processor.extract_career_related_terms(prompt)
        
        # Update user profile with extracted information
        if 'chat_keywords' not in st.session_state.user_profile:
            st.session_state.user_profile['chat_keywords'] = []
        
        # Add new keywords, avoiding duplicates
        existing_keywords = set(st.session_state.user_profile['chat_keywords'])
        new_keywords = [kw for kw in keywords if kw not in existing_keywords]
        st.session_state.user_profile['chat_keywords'].extend(new_keywords)
        
        # Store additional NLP insights
        st.session_state.user_profile['sentiment'] = sentiment
        st.session_state.user_profile['career_terms'] = career_terms
        
        # Generate intelligent response based on question type
        if question_type in ['question', 'information_request']:
            # Use career Q&A system for questions
            question_analysis = self.qa_system.analyze_question(prompt)
            response = self.qa_system.generate_answer(question_analysis)
        else:
            # Use conversational response for statements
            response = self._generate_response(prompt, keywords, sentiment, career_terms)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display the new messages
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response)
    
    def _generate_response(self, user_input, keywords, sentiment='neutral', career_terms=None):
        """Generate contextual response based on user input and extracted information"""
        
        if career_terms is None:
            career_terms = {}
        
        # Create a contextual response based on keywords and sentiment
        if not keywords and not any(career_terms.values()):
            return """I understand you're looking for career guidance! Could you tell me more specifically about:
            
• What subjects or activities do you enjoy?
• What are your strongest skills?
• What type of work environment appeals to you?
• Any particular industries that interest you?

You can also ask me specific questions like:
• "What's the salary for a software developer?"
• "What education do I need to become a nurse?"
• "What are the trends in the technology industry?"

The more details you share, the better I can help you find the perfect career path!"""
        
        # Build response based on sentiment and extracted information
        response_parts = []
        
        # Acknowledge sentiment
        if sentiment == 'positive':
            response_parts.append("I can sense your enthusiasm! That's wonderful.")
        elif sentiment == 'negative':
            response_parts.append("I understand you might have some concerns. Let me help address them.")
        
        # Acknowledge interests and skills
        if keywords:
            response_parts.append(f"I can see you're interested in: **{', '.join(keywords[:5])}**")
        
        # Acknowledge specific career-related information
        if career_terms.get('skills'):
            response_parts.append(f"You mentioned skills like: {', '.join(career_terms['skills'][:3])}")
        
        if career_terms.get('interests'):
            response_parts.append(f"Your interests include: {', '.join(career_terms['interests'][:3])}")
        
        if career_terms.get('goals'):
            response_parts.append(f"I notice you have goals related to: {', '.join(career_terms['goals'][:3])}")
        
        response_parts.append("")
        response_parts.append("Based on what you've shared, here are some ways I can help:")
        response_parts.append("")
        
        # Add contextual suggestions based on keywords
        tech_keywords = ['coding', 'programming', 'computer', 'software', 'technology', 'data']
        creative_keywords = ['art', 'design', 'creative', 'drawing', 'music', 'writing']
        business_keywords = ['business', 'management', 'marketing', 'finance', 'entrepreneurship']
        people_keywords = ['teaching', 'helping', 'communication', 'social', 'psychology']
        
        if any(kw in keywords for kw in tech_keywords):
            response_parts.append("• Ask me about technology careers, required skills, or salary ranges")
        if any(kw in keywords for kw in creative_keywords):
            response_parts.append("• Explore creative career paths and portfolio requirements")
        if any(kw in keywords for kw in business_keywords):
            response_parts.append("• Learn about business careers and entrepreneurship opportunities")
        if any(kw in keywords for kw in people_keywords):
            response_parts.append("• Discover people-focused careers in education, healthcare, or counseling")
        
        response_parts.extend([
            "",
            "You can ask specific questions or click **'Get Career Recommendations'** for personalized suggestions!"
        ])
        
        return "\n".join(response_parts)
