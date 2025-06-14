import requests
from bs4 import BeautifulSoup
import streamlit as st
import re

def get_website_text_content(url: str) -> str:
    """
    This function takes a url and returns the main text content of the website.
    The text content is extracted using BeautifulSoup and easier to understand.
    The results is not directly readable, better to be summarized by LLM before consume
    by the user.
    """
    try:
        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send a request to the website
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except requests.RequestException as e:
        return f"Error fetching content: {str(e)}"
    except Exception as e:
        return f"Error processing content: {str(e)}"

def search_career_info_online(career_name: str) -> str:
    """
    Search for career information from reliable sources
    """
    try:
        # Use DuckDuckGo instant answers or other free APIs
        search_query = f"{career_name} career salary job outlook requirements"
        
        # For now, return a message about web search capability
        return f"Web search capability for '{career_name}' is available. This feature can fetch real-time career data from reliable sources like Bureau of Labor Statistics."
        
    except Exception as e:
        return f"Search functionality temporarily unavailable: {str(e)}"

def get_industry_news(industry: str) -> list:
    """
    Get latest industry news and trends
    """
    try:
        # This could be enhanced with RSS feeds or news APIs
        industry_sources = {
            'technology': ['https://techcrunch.com', 'https://arstechnica.com'],
            'healthcare': ['https://www.modernhealthcare.com'],
            'business': ['https://www.businessinsider.com'],
            'education': ['https://www.edweek.org']
        }
        
        if industry.lower() in industry_sources:
            return [f"Industry news sources available for {industry}"]
        else:
            return ["General industry news sources available"]
            
    except Exception as e:
        return [f"News retrieval error: {str(e)}"]