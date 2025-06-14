import re
import streamlit as st
from data.career_knowledge_base import (
    get_career_info, get_course_info, get_industry_trends, 
    search_careers_by_skill, get_salary_comparison, CAREER_KNOWLEDGE_BASE
)
from utils.web_scraper import get_website_text_content

class CareerQASystem:
    def __init__(self):
        self.question_patterns = {
            'salary': [
                r'salary|pay|earn|income|money|wage',
                r'how much.*make|how much.*earn|what.*pay'
            ],
            'education': [
                r'education|degree|study|learn|school|college|university',
                r'what.*study|how.*become|requirements'
            ],
            'skills': [
                r'skills|abilities|qualifications|competencies',
                r'what.*skills|need.*skills'
            ],
            'job_outlook': [
                r'outlook|future|growth|demand|opportunities',
                r'job.*market|career.*prospects'
            ],
            'work_environment': [
                r'work.*environment|workplace|office|remote',
                r'where.*work|work.*conditions'
            ],
            'career_comparison': [
                r'compare|versus|vs|difference|better',
                r'which.*career|compare.*careers'
            ],
            'course_info': [
                r'course|program|curriculum|subjects',
                r'what.*course|which.*program'
            ],
            'industry_trends': [
                r'trends|future|emerging|technology|innovation',
                r'industry.*trends|what.*happening'
            ]
        }
    
    def analyze_question(self, question):
        """Analyze the user's question to determine intent and extract entities"""
        question_lower = question.lower()
        
        # Determine question type
        question_type = 'general'
        for qtype, patterns in self.question_patterns.items():
            for pattern in patterns:
                if re.search(pattern, question_lower):
                    question_type = qtype
                    break
            if question_type != 'general':
                break
        
        # Extract career/course names
        entities = self._extract_entities(question_lower)
        
        return {
            'type': question_type,
            'entities': entities,
            'original_question': question
        }
    
    def _extract_entities(self, text):
        """Extract career and course names from the question"""
        entities = {'careers': [], 'courses': [], 'skills': []}
        
        # Common career terms
        career_terms = [
            'software developer', 'data scientist', 'nurse', 'teacher', 'doctor',
            'engineer', 'manager', 'analyst', 'designer', 'writer', 'programmer',
            'developer', 'marketing', 'finance', 'accounting', 'psychology',
            'cybersecurity', 'physical therapist', 'graphic designer'
        ]
        
        # Common course terms
        course_terms = [
            'computer science', 'business administration', 'nursing', 'marketing',
            'engineering', 'psychology', 'medicine', 'education', 'finance',
            'graphic design', 'journalism', 'biology', 'chemistry', 'physics'
        ]
        
        # Common skills
        skill_terms = [
            'programming', 'coding', 'leadership', 'communication', 'analytical',
            'creative', 'problem solving', 'teamwork', 'organization'
        ]
        
        for career in career_terms:
            if career in text:
                entities['careers'].append(career)
        
        for course in course_terms:
            if course in text:
                entities['courses'].append(course)
        
        for skill in skill_terms:
            if skill in text:
                entities['skills'].append(skill)
        
        return entities
    
    def generate_answer(self, analysis):
        """Generate a comprehensive answer based on question analysis"""
        question_type = analysis['type']
        entities = analysis['entities']
        
        if question_type == 'salary' and entities['careers']:
            return self._answer_salary_question(entities['careers'])
        
        elif question_type == 'education' and entities['careers']:
            return self._answer_education_question(entities['careers'])
        
        elif question_type == 'skills' and entities['careers']:
            return self._answer_skills_question(entities['careers'])
        
        elif question_type == 'job_outlook' and entities['careers']:
            return self._answer_job_outlook_question(entities['careers'])
        
        elif question_type == 'work_environment' and entities['careers']:
            return self._answer_work_environment_question(entities['careers'])
        
        elif question_type == 'career_comparison' and len(entities['careers']) >= 2:
            return self._answer_comparison_question(entities['careers'])
        
        elif question_type == 'course_info' and entities['courses']:
            return self._answer_course_question(entities['courses'])
        
        elif question_type == 'industry_trends':
            return self._answer_trends_question(entities)
        
        elif entities['skills']:
            return self._answer_skills_based_career_search(entities['skills'])
        
        else:
            return self._generate_general_career_guidance()
    
    def _answer_salary_question(self, careers):
        """Answer salary-related questions"""
        response = "Here's salary information for the careers you asked about:\n\n"
        
        for career in careers[:3]:  # Limit to 3 careers
            career_info = get_career_info(career)
            if career_info:
                response += f"**{career.title()}:**\n"
                response += f"• Salary Range: {career_info['salary_range']}\n"
                response += f"• Job Outlook: {career_info['job_outlook']}\n\n"
        
        response += "Salaries can vary based on location, experience, education, and company size."
        return response
    
    def _answer_education_question(self, careers):
        """Answer education-related questions"""
        response = "Here are the education requirements:\n\n"
        
        for career in careers[:3]:
            career_info = get_career_info(career)
            if career_info:
                response += f"**{career.title()}:**\n"
                response += f"• Education: {career_info['education']}\n"
                response += f"• Key Skills: {', '.join(career_info['skills_required'][:5])}\n\n"
        
        return response
    
    def _answer_skills_question(self, careers):
        """Answer skills-related questions"""
        response = "Here are the key skills needed:\n\n"
        
        for career in careers[:3]:
            career_info = get_career_info(career)
            if career_info:
                response += f"**{career.title()}:**\n"
                response += f"• Required Skills: {', '.join(career_info['skills_required'])}\n"
                response += f"• Work Environment: {career_info['work_environment']}\n\n"
        
        return response
    
    def _answer_job_outlook_question(self, careers):
        """Answer job outlook questions"""
        response = "Here's the job market outlook:\n\n"
        
        for career in careers[:3]:
            career_info = get_career_info(career)
            if career_info:
                response += f"**{career.title()}:**\n"
                response += f"• Job Outlook: {career_info['job_outlook']}\n"
                response += f"• Related Careers: {', '.join(career_info.get('related_careers', [])[:3])}\n\n"
        
        return response
    
    def _answer_work_environment_question(self, careers):
        """Answer work environment questions"""
        response = "Here's information about work environments:\n\n"
        
        for career in careers[:3]:
            career_info = get_career_info(career)
            if career_info:
                response += f"**{career.title()}:**\n"
                response += f"• Work Environment: {career_info['work_environment']}\n"
                response += f"• Description: {career_info['description'][:150]}...\n\n"
        
        return response
    
    def _answer_comparison_question(self, careers):
        """Compare multiple careers"""
        response = "Here's a comparison of these careers:\n\n"
        
        comparison_data = get_salary_comparison(careers[:3])
        
        for item in comparison_data:
            response += f"**{item['career']}:**\n"
            response += f"• Salary: {item['salary_range']}\n"
            response += f"• Outlook: {item['job_outlook']}\n\n"
        
        return response
    
    def _answer_course_question(self, courses):
        """Answer course-related questions"""
        response = "Here's information about these courses:\n\n"
        
        for course in courses[:3]:
            course_info = get_course_info(course)
            if course_info:
                response += f"**{course.title()}:**\n"
                response += f"• Duration: {course_info['duration']}\n"
                response += f"• Core Subjects: {', '.join(course_info['core_subjects'][:5])}\n"
                response += f"• Career Paths: {', '.join(course_info['career_paths'][:4])}\n\n"
        
        return response
    
    def _answer_trends_question(self, entities):
        """Answer industry trends questions"""
        response = "Here are current industry trends:\n\n"
        
        # Determine industry from entities
        industries = ['technology', 'healthcare', 'business', 'education']
        
        for industry in industries:
            trends = get_industry_trends(industry)
            if trends:
                response += f"**{industry.title()} Industry:**\n"
                for trend in trends[:3]:
                    response += f"• {trend}\n"
                response += "\n"
        
        return response
    
    def _answer_skills_based_career_search(self, skills):
        """Find careers based on skills"""
        response = "Based on your skills, here are suitable careers:\n\n"
        
        all_matching_careers = []
        for skill in skills:
            matching = search_careers_by_skill(skill)
            all_matching_careers.extend(matching)
        
        # Remove duplicates
        unique_careers = []
        seen = set()
        for career in all_matching_careers:
            if career['name'] not in seen:
                unique_careers.append(career)
                seen.add(career['name'])
        
        for career in unique_careers[:5]:
            response += f"**{career['name']}:**\n"
            response += f"• Category: {career['category'].title()}\n"
            response += f"• Description: {career['description'][:120]}...\n\n"
        
        return response
    
    def _generate_general_career_guidance(self):
        """Generate general career guidance"""
        return """I can help you with career questions! Here are some topics I can assist with:

**Career Information:**
• Salary ranges and job outlook
• Education requirements and skills needed
• Work environments and job responsibilities
• Career comparisons and alternatives

**Course Guidance:**
• Program details and duration
• Core subjects and curriculum
• Career paths after graduation
• Admission requirements

**Industry Insights:**
• Current trends and future outlook
• Emerging opportunities
• Skills in demand

Feel free to ask specific questions like:
• "What's the salary for a software developer?"
• "What education do I need to become a nurse?"
• "Compare marketing manager vs financial analyst"
• "What are the trends in technology industry?"

How can I help you with your career exploration?"""

    def get_web_enhanced_answer(self, question, base_answer):
        """Enhance answer with web search results for current information"""
        try:
            # Try to get additional information from reliable career websites
            search_queries = self._generate_search_queries(question)
            
            additional_info = ""
            for query_url in search_queries[:2]:  # Limit to 2 sources
                try:
                    content = get_website_text_content(query_url)
                    if content and len(content) > 100:
                        # Extract relevant snippets
                        relevant_snippet = self._extract_relevant_snippet(content, question)
                        if relevant_snippet:
                            additional_info += f"\n\n**Additional Current Information:**\n{relevant_snippet}"
                        break
                except:
                    continue
            
            return base_answer + additional_info
            
        except Exception as e:
            return base_answer
    
    def _generate_search_queries(self, question):
        """Generate search URLs for reliable career information"""
        # Use Bureau of Labor Statistics and other reliable sources
        base_urls = [
            "https://www.bls.gov/ooh/",  # Bureau of Labor Statistics
        ]
        
        return base_urls
    
    def _extract_relevant_snippet(self, content, question):
        """Extract relevant information from web content"""
        # Simple relevance extraction based on question keywords
        sentences = content.split('.')[:10]  # First 10 sentences
        relevant = []
        
        question_words = question.lower().split()
        for sentence in sentences:
            if any(word in sentence.lower() for word in question_words):
                relevant.append(sentence.strip())
        
        if relevant:
            return '. '.join(relevant[:3]) + '.'
        
        return None