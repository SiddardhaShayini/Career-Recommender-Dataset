import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from data.interests_mapping import INTEREST_KEYWORDS
import streamlit as st
from collections import Counter

# Download required NLTK data
@st.cache_resource
def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
    
    # Also download punkt_tab for newer NLTK versions
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')
    
    # Download additional NLP data
    try:
        nltk.data.find('taggers/averaged_perceptron_tagger')
        nltk.data.find('chunkers/maxent_ne_chunker')
        nltk.data.find('corpora/words')
    except LookupError:
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')

class TextProcessor:
    def __init__(self):
        download_nltk_data()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess_text(self, text):
        """Clean and preprocess text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        processed_tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token not in self.stop_words and len(token) > 2
        ]
        
        return processed_tokens
    
    def extract_keywords(self, text):
        """Extract relevant keywords from user input"""
        processed_tokens = self.preprocess_text(text)
        
        # Find matches with predefined interest keywords
        matched_keywords = []
        
        for interest, keywords in INTEREST_KEYWORDS.items():
            for keyword in keywords:
                if keyword in processed_tokens or keyword in text.lower():
                    matched_keywords.append(interest)
                    break
        
        # Also include significant tokens that might be relevant
        significant_tokens = [
            token for token in processed_tokens 
            if len(token) > 3 and token not in matched_keywords
        ]
        
        # Combine and remove duplicates
        all_keywords = list(set(matched_keywords + significant_tokens[:5]))  # Limit to top 5 additional tokens
        
        return all_keywords
    
    def text_to_feature_vector(self, text, user_profile=None):
        """Convert text input to feature vector for model prediction"""
        # Initialize feature vector with zeros (59 features based on dataset)
        feature_vector = [0] * 59
        
        # Extract keywords from text
        keywords = self.extract_keywords(text)
        
        # Map keywords to feature indices
        for keyword in keywords:
            if keyword in INTEREST_KEYWORDS:
                # Find the index of this interest in the feature vector
                try:
                    from data.interests_mapping import INTERESTS_LIST
                    if keyword in INTERESTS_LIST:
                        idx = INTERESTS_LIST.index(keyword)
                        if idx < len(feature_vector):
                            feature_vector[idx] = 1
                except (ValueError, IndexError):
                    continue
        
        # Include selected interests from user profile
        if user_profile and 'selected_interests' in user_profile:
            for interest in user_profile['selected_interests']:
                try:
                    from data.interests_mapping import INTERESTS_LIST
                    if interest in INTERESTS_LIST:
                        idx = INTERESTS_LIST.index(interest)
                        if idx < len(feature_vector):
                            feature_vector[idx] = 1
                except (ValueError, IndexError):
                    continue
        
        return feature_vector
    
    def extract_named_entities(self, text):
        """Extract named entities from text using NLTK"""
        try:
            tokens = word_tokenize(text)
            pos_tags = pos_tag(tokens)
            named_entities = ne_chunk(pos_tags)
            
            entities = []
            for chunk in named_entities:
                if hasattr(chunk, 'label'):
                    entity = ' '.join([token for token, pos in chunk.leaves()])
                    entities.append({'text': entity, 'label': chunk.label()})
            
            return entities
        except Exception:
            return []
    
    def get_text_sentiment(self, text):
        """Basic sentiment analysis using keyword matching"""
        positive_words = ['love', 'enjoy', 'like', 'passionate', 'excited', 'interested', 'good', 'great', 'amazing']
        negative_words = ['hate', 'dislike', 'boring', 'difficult', 'hard', 'bad', 'terrible', 'awful']
        
        words = self.preprocess_text(text)
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def extract_career_related_terms(self, text):
        """Extract career-related terms from text"""
        career_terms = {
            'skills': ['skill', 'ability', 'talent', 'expertise', 'competency', 'proficiency'],
            'interests': ['interest', 'passion', 'hobby', 'enjoy', 'love', 'like'],
            'experience': ['experience', 'worked', 'job', 'internship', 'volunteer', 'project'],
            'education': ['degree', 'study', 'major', 'course', 'school', 'college', 'university'],
            'goals': ['want', 'goal', 'aspire', 'dream', 'hope', 'plan', 'future']
        }
        
        words = self.preprocess_text(text)
        found_terms = {}
        
        for category, terms in career_terms.items():
            found_terms[category] = [word for word in words if word in terms]
        
        return found_terms
    
    def get_question_type(self, text):
        """Identify if the text is a question and what type"""
        question_words = ['what', 'how', 'why', 'when', 'where', 'which', 'who']
        text_lower = text.lower()
        
        if text.endswith('?'):
            return 'question'
        
        if any(text_lower.startswith(word) for word in question_words):
            return 'question'
        
        if any(word in text_lower for word in ['tell me', 'can you', 'do you know']):
            return 'information_request'
        
        return 'statement'
    
    def extract_key_phrases(self, text):
        """Extract key phrases using simple n-gram analysis"""
        words = word_tokenize(text.lower())
        
        # Remove stopwords and non-alphabetic tokens
        filtered_words = [word for word in words if word.isalpha() and word not in self.stop_words]
        
        # Get bigrams and trigrams
        bigrams = [f"{filtered_words[i]} {filtered_words[i+1]}" 
                  for i in range(len(filtered_words)-1)]
        trigrams = [f"{filtered_words[i]} {filtered_words[i+1]} {filtered_words[i+2]}" 
                   for i in range(len(filtered_words)-2)]
        
        # Count frequency
        all_phrases = filtered_words + bigrams + trigrams
        phrase_freq = Counter(all_phrases)
        
        # Return top phrases
        return [phrase for phrase, count in phrase_freq.most_common(10) if count > 1]
