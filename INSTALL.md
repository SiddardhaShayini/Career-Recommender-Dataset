# Installation Guide

## Dependencies

Create a `requirements.txt` file with the following contents:

```txt
streamlit>=1.28.0
nltk>=3.8.1
scikit-learn>=1.3.0
tensorflow==2.11.0
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
beautifulsoup4>=4.12.0
joblib>=1.3.0
trafilatura>=1.6.0
```

## Installation Steps

### Windows
```cmd
# Clone the repository
git clone <repository-url>
cd ai-career-counsellor

# Create virtual environment
python -m venv career_env

# Activate virtual environment
career_env\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (run once)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words')"

# Run the application
streamlit run app.py
```

### macOS/Linux
```bash
# Clone the repository
git clone <repository-url>
cd ai-career-counsellor

# Create virtual environment
python3 -m venv career_env

# Activate virtual environment
source career_env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (run once)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words')"

# Run the application
streamlit run app.py
```

### Using conda (Alternative)
```bash
# Create conda environment
conda create -n career_env python=3.11
conda activate career_env

# Install packages
conda install streamlit pandas numpy scikit-learn
pip install nltk tensorflow requests beautifulsoup4 joblib trafilatura

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words')"

# Run application
streamlit run app.py
```

## Troubleshooting

### Common Issues

1. **TensorFlow Installation Issues**
   ```bash
   # For M1/M2 Macs
   pip install tensorflow-macos
   
   # For older systems
   pip install tensorflow==2.13.0
   ```

2. **NLTK Data Download Issues**
   ```python
   import nltk
   import ssl
   
   try:
       _create_unverified_https_context = ssl._create_unverified_context
   except AttributeError:
       pass
   else:
       ssl._create_default_https_context = _create_unverified_https_context
   
   nltk.download('punkt')
   # ... other downloads
   ```

3. **Port Already in Use**
   ```bash
   streamlit run app.py --server.port 8502
   ```

4. **Memory Issues with Large Models**
   - Ensure at least 4GB RAM available
   - Close other applications
   - Use fallback recommendations if models fail to load

### Verification

After installation, verify everything works:

```bash
python -c "
import streamlit as st
import nltk
import sklearn
import pandas as pd
import numpy as np
print('All packages imported successfully!')
"
```

## Configuration

Create `.streamlit/config.toml`:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[browser]
gatherUsageStats = false
```
