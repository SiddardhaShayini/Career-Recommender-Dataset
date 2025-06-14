# 🎯 AI Virtual Career Counsellor

An intelligent, AI-powered career counselling application that provides personalized career path and course recommendations based on user interests, skills, and goals. Built with Streamlit and enhanced with advanced Natural Language Processing capabilities.

![Career Counsellor Demo](https://img.shields.io/badge/Status-Active-green) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### Core Functionality
- **Dual Input Methods**: Chat interface and checklist-based interest selection
- **Intelligent Q&A System**: Answers specific career questions with comprehensive information
- **Personalized Recommendations**: ML-powered course and career suggestions
- **Real-time Career Data**: Salary ranges, job outlook, education requirements
- **Interactive Chat Interface**: Natural language processing for conversational career guidance

### Advanced NLP Features
- **Sentiment Analysis**: Understands user emotions and enthusiasm levels
- **Named Entity Recognition**: Extracts key career-related terms from conversations
- **Keyword Extraction**: Identifies interests and skills from natural language input
- **Question Classification**: Automatically detects and routes different types of queries
- **Career Term Analysis**: Categorizes user input into skills, interests, experience, education, and goals

### Career Knowledge Base
- **Comprehensive Career Database**: 15+ detailed career profiles across technology, healthcare, business, education, and creative fields
- **Industry Insights**: Current trends and future outlook for major industries
- **Salary Information**: Real salary ranges and job market data
- **Education Guidance**: Detailed course information, duration, and career paths
- **Skills Mapping**: Required skills and competencies for each career path

### User Experience
- **Clear Interface**: Easy-to-use buttons for clearing chat history and profile data
- **Example Prompts**: Pre-built examples for both interest sharing and career questions
- **Profile Summary**: Real-time display of extracted interests and keywords
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## 🛠️ Technology Stack

### Frontend
- **Streamlit**: Modern web application framework for Python
- **HTML/CSS**: Custom styling and responsive design
- **JavaScript**: Interactive elements and real-time updates

### Backend & AI
- **Python 3.11**: Core programming language
- **NLTK**: Natural Language Processing toolkit
  - Tokenization and text preprocessing
  - Sentiment analysis
  - Named entity recognition
  - Part-of-speech tagging
- **Scikit-learn**: Machine learning models
  - Random Forest for course recommendations
  - Label encoding for categorical data
  - Feature vector processing
- **TensorFlow/Keras**: Deep learning models (with fallback support)
- **Pandas & NumPy**: Data manipulation and numerical computing

### Data Sources & Storage
- **CSV Dataset**: Cleaned career and course data (3,500+ records)
- **Pickle Models**: Pre-trained ML models for recommendations
- **Knowledge Base**: Structured career information database
- **Session State**: Real-time user profile management

### Web Integration
- **Requests & BeautifulSoup**: Web scraping capabilities for current career information
- **RESTful Architecture**: Modular design for easy API integration

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                       │
├─────────────────────────────────────────────────────────────┤
│  Chat Interface  │  Interest Selection  │  Profile Summary │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                  Core Processing Layer                      │
├─────────────────┬─────────────────┬─────────────────────────┤
│ Text Processor  │ Career Q&A     │ Recommendation Engine   │
│ - NLTK         │ - Knowledge DB  │ - ML Models            │
│ - Sentiment    │ - Web Scraping  │ - Fallback Rules       │
│ - NER          │ - Pattern Match │ - Feature Vectors      │
└─────────────────┴─────────────────┴─────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                               │
├─────────────────┬─────────────────┬─────────────────────────┤
│ ML Models       │ Knowledge Base  │ User Data              │
│ - Course Model  │ - Career Info   │ - Session State        │
│ - Career Model  │ - Industry      │ - Profile Summary      │
│ - Encoders      │ - Trends        │ - Chat History         │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 📋 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Local Installation

#### Windows
```bash
# Clone the repository
git clone <repository-url>
cd ai-career-counsellor

# Create virtual environment
python -m venv career_env

# Activate virtual environment
career_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

#### macOS/Linux
```bash
# Clone the repository
git clone <repository-url>
cd ai-career-counsellor

# Create virtual environment
python3 -m venv career_env

# Activate virtual environment
source career_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Requirements.txt
```
streamlit>=1.28.0
nltk>=3.8.1
scikit-learn>=1.3.0
tensorflow>=2.13.0
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
beautifulsoup4>=4.12.0
joblib>=1.3.0
```

### Alternative Installation (Using uv)
```bash
# Install uv package manager
pip install uv

# Install dependencies
uv add streamlit nltk scikit-learn tensorflow pandas numpy requests beautifulsoup4

# Run application
streamlit run app.py --server.port 5000
```

## 🚀 Running the Application

### Development Mode
```bash
# Start the Streamlit server
streamlit run app.py

# With custom configuration
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Production Deployment
```bash
# Using Streamlit Cloud
# Push to GitHub and connect via streamlit.io

# Using Docker
docker build -t career-counsellor .
docker run -p 8501:8501 career-counsellor

# Using Replit (Current deployment)
# Configured for autoscale deployment
```

### Configuration
Create `.streamlit/config.toml`:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
```

## 💡 Usage Guide

### Getting Started
1. **Launch the Application**: Navigate to the web interface
2. **Choose Input Method**: 
   - Chat with AI for natural conversation
   - Select from checklist for structured input
   - Use both methods for comprehensive profiling

### Chat Interface
- **Ask Questions**: "What's the salary for a software developer?"
- **Share Interests**: "I love coding and solving problems"
- **Get Comparisons**: "Compare marketing manager vs financial analyst"
- **Industry Insights**: "What are the trends in technology industry?"

### Interest Selection
- **Browse Categories**: 59 predefined interests across multiple domains
- **Multiple Selection**: Choose as many interests as applicable
- **Clear Options**: Reset selections with one click

### Getting Recommendations
1. **Build Your Profile**: Chat or select interests
2. **Review Summary**: Check extracted keywords and interests
3. **Get Recommendations**: Click the recommendation button
4. **Explore Results**: View course and career suggestions

## 🧠 AI & Machine Learning Components

### Natural Language Processing
- **Text Preprocessing**: Tokenization, lemmatization, stopword removal
- **Sentiment Analysis**: Positive, negative, neutral emotion detection
- **Named Entity Recognition**: Extraction of career-related entities
- **Question Classification**: Automatic routing of different query types
- **Keyword Extraction**: Interest and skill identification from text

### Machine Learning Models
- **Random Forest Classifier**: Course recommendation (Scikit-learn)
- **Neural Network**: Career path prediction (TensorFlow/Keras)
- **Label Encoders**: Categorical data processing
- **Fallback System**: Rule-based recommendations when ML models unavailable

### Knowledge Base
- **Structured Data**: 15+ career profiles with detailed information
- **Industry Trends**: Current market insights and future outlook
- **Salary Data**: Real compensation ranges and growth projections
- **Education Mapping**: Course-to-career pathway recommendations

## 📈 Performance & Scalability

### Optimization Features
- **Caching**: NLTK data and model loading optimization
- **Session Management**: Efficient user state handling
- **Lazy Loading**: Models loaded only when needed
- **Error Handling**: Graceful fallbacks for system failures

### Scalability Considerations
- **Modular Architecture**: Easy to extend with new features
- **API-Ready Design**: Prepared for microservices architecture
- **Database Integration**: Structured for future database connectivity
- **Cloud Deployment**: Optimized for autoscale environments

## 🔧 Development

### Project Structure
```
ai-career-counsellor/
├── app.py                          # Main application entry point
├── components/
│   └── chat_interface.py          # Chat UI and interaction logic
├── utils/
│   ├── text_processor.py          # NLP processing utilities
│   ├── career_recommender.py      # ML recommendation engine
│   ├── career_qa_system.py        # Intelligent Q&A system
│   └── web_scraper.py             # Web data extraction
├── models/
│   └── model_loader.py            # ML model management
├── data/
│   ├── interests_mapping.py       # Interest categories and keywords
│   └── career_knowledge_base.py   # Comprehensive career database
├── attached_assets/               # Pre-trained models and datasets
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── requirements.txt               # Python dependencies
├── replit.md                      # Project documentation
└── README.md                      # This file
```

### Adding New Features

#### New Career Information
1. **Update Knowledge Base**: Add entries to `data/career_knowledge_base.py`
2. **Enhance Keywords**: Update `data/interests_mapping.py`
3. **Test Integration**: Verify Q&A system responses

#### New NLP Features
1. **Extend Text Processor**: Add methods to `utils/text_processor.py`
2. **Update Chat Interface**: Integrate new features in `components/chat_interface.py`
3. **Test Functionality**: Validate with various input types

#### New ML Models
1. **Train Models**: Use provided dataset structure
2. **Update Model Loader**: Add loading functions in `models/model_loader.py`
3. **Integrate Predictions**: Connect to recommendation engine

### Code Quality Standards
- **PEP 8**: Python style guide compliance
- **Type Hints**: Function parameter and return type annotations
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Graceful failure management
- **Testing**: Unit tests for core functionality

## 🔮 Future Development

### Short-term Enhancements (v2.0)
- **Advanced ML Models**: Integration of transformer-based language models
- **Multi-language Support**: Internationalization for global users
- **Enhanced UI**: Modern design system and improved user experience
- **Mobile Optimization**: Native mobile app development
- **Real-time Data**: Live job market and salary information integration

### Medium-term Goals (v3.0)
- **Personalized Learning Paths**: Custom education roadmaps
- **Industry Connections**: Integration with job boards and networking platforms
- **Assessment Tools**: Skills testing and personality assessments
- **Mentorship Matching**: Connect users with industry professionals
- **Progress Tracking**: Career development journey monitoring

### Long-term Vision (v4.0)
- **AI Coaching**: Advanced conversational AI for ongoing career support
- **Predictive Analytics**: Future career trend predictions
- **Virtual Reality**: Immersive career exploration experiences
- **Blockchain Credentials**: Secure skill and achievement verification
- **Global Platform**: International career guidance and opportunities

### Technical Roadmap
- **Microservices Architecture**: Scalable backend services
- **GraphQL API**: Flexible data querying capabilities
- **Machine Learning Pipeline**: Automated model training and deployment
- **Cloud-Native Deployment**: Kubernetes orchestration
- **Data Lake Integration**: Big data analytics and insights

## 🤝 Contributing

### Development Process
1. **Fork Repository**: Create your development branch
2. **Follow Standards**: Adhere to code quality guidelines
3. **Add Tests**: Include unit tests for new features
4. **Update Documentation**: Maintain README and inline documentation
5. **Submit Pull Request**: Detailed description of changes

### Bug Reports
- **Issue Template**: Use provided GitHub issue templates
- **Reproduction Steps**: Clear steps to reproduce the problem
- **Environment Info**: Python version, OS, and package versions
- **Expected vs Actual**: Clear description of the issue

### Feature Requests
- **Use Case Description**: Explain the problem being solved
- **Proposed Solution**: Detailed implementation suggestions
- **Alternative Approaches**: Consider multiple solutions
- **Impact Assessment**: Benefits and potential drawbacks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-party Licenses
- **NLTK**: Apache License 2.0
- **Scikit-learn**: BSD 3-Clause License
- **TensorFlow**: Apache License 2.0
- **Streamlit**: Apache License 2.0
- **Pandas**: BSD 3-Clause License

## 🙏 Acknowledgments

### Open Source Libraries
- **NLTK Team**: Natural language processing capabilities
- **Scikit-learn Contributors**: Machine learning framework
- **Streamlit Team**: Web application framework
- **TensorFlow Community**: Deep learning infrastructure

### Data Sources
- **Bureau of Labor Statistics**: Career outlook and salary data
- **Educational Institutions**: Course curriculum information
- **Industry Reports**: Market trends and insights

### Special Thanks
- **Career Counselling Professionals**: Domain expertise and validation
- **Beta Testers**: Feedback and improvement suggestions
- **Open Source Community**: Continuous support and contributions

## 📞 Support & Contact

### Documentation
- **User Guide**: Comprehensive usage instructions
- **Developer Docs**: Technical implementation details
- **API Reference**: Complete function and method documentation
- **FAQ**: Common questions and troubleshooting

### Community
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: Community forum for questions and ideas
- **Contributing Guide**: How to get involved in development

### Professional Support
- **Consulting**: Custom implementation and integration services
- **Training**: Workshops and educational programs
- **Enterprise**: Commercial licensing and support options

---

**Built with ❤️ for career guidance and professional development**

*Last Updated: June 14, 2025*
*Version: 1.2.0*
*Status: Active Development*