# Streamlit Cloud Deployment Guide

## Quick Deploy

1. **Push to GitHub**: Ensure all files are committed and pushed to your GitHub repository
2. **Connect to Streamlit Cloud**: 
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select repository: `career-recommender-dataset`
   - Branch: `main`
   - Main file path: `app.py`

## Deployment Files

The following files are configured for Streamlit Cloud:

### `.streamlit/requirements.txt`
```
streamlit>=1.28.0
nltk>=3.8.1
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
beautifulsoup4>=4.12.0
joblib>=1.3.0
trafilatura>=1.6.0
```

### `packages.txt` (System Dependencies)
```
build-essential
python3-dev
```

### `runtime.txt` (Python Version)
```
python-3.9
```

### `.streamlit/config.toml` (App Configuration)
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
```

## Important Notes

1. **No TensorFlow**: The app uses scikit-learn models and intelligent rule-based recommendations instead of TensorFlow for compatibility
2. **NLTK Data**: Downloads automatically on first run
3. **Python Version**: Configured for Python 3.9 for maximum compatibility
4. **Dependencies**: All packages are compatible with Streamlit Cloud's environment

## Troubleshooting

If deployment fails:

1. **Check logs** in Streamlit Cloud dashboard
2. **Verify GitHub sync** - ensure latest code is pushed
3. **Dependencies** - all packages in requirements.txt must be available
4. **Python version** - must match runtime.txt specification

## Alternative Deployment Options

### Local Development
```bash
git clone <repository-url>
cd ai-career-counsellor
pip install -r .streamlit/requirements.txt
streamlit run app.py
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r .streamlit/requirements.txt
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Heroku Deployment
1. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Use `.streamlit/requirements.txt` as `requirements.txt`
3. Deploy via Heroku CLI or GitHub integration

## Environment Variables

No external API keys required - the app uses:
- Built-in career knowledge base
- Local ML models (scikit-learn)
- Rule-based recommendation system
- NLTK for text processing

## Performance Notes

- First load may take 30-60 seconds for NLTK data download
- Models load from cached pickle files for fast response
- Fallback recommendations ensure system reliability
- Optimized for Streamlit Cloud's resource limits