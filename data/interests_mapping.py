# List of 59 interests/skills based on the dataset
INTERESTS_LIST = [
    'Drawing', 'Dancing', 'Singing', 'Sports', 'Video_Game', 'Acting', 'Travelling',
    'Gardening', 'Animals', 'Photography', 'Teaching', 'Exercise', 'Coding',
    'Electricity_Components', 'Mechanic_Parts', 'Computer_Parts', 'Researching',
    'Architecture', 'Historic_Collection', 'Botany', 'Zoology', 'Physics',
    'Accounting', 'Economics', 'Sociology', 'Geography', 'Psychology', 'History',
    'Science', 'Bussiness_Education', 'Chemistry', 'Mathematics', 'Biology',
    'Makeup', 'Designing', 'Content_Writing', 'Crafting', 'Literature', 'Reading',
    'Cartooning', 'Debating', 'Astrology', 'Hindi', 'French', 'English', 'Urdu',
    'Other_Language', 'Makeup_Artist', 'Mechanic', 'Model', 'Sales', 'Doctor',
    'Pharmacist', 'Cycling', 'Knitting', 'Director', 'Journalism', 'Business',
    'Listening_Music'
]

# Keyword mapping for natural language processing
INTEREST_KEYWORDS = {
    'Drawing': ['draw', 'drawing', 'sketch', 'sketching', 'illustration', 'art', 'artistic'],
    'Dancing': ['dance', 'dancing', 'choreography', 'ballet', 'performance'],
    'Singing': ['sing', 'singing', 'music', 'vocal', 'song', 'choir'],
    'Sports': ['sport', 'sports', 'athletics', 'fitness', 'games', 'competition'],
    'Video_Game': ['gaming', 'games', 'video game', 'esports', 'game development'],
    'Acting': ['acting', 'theater', 'drama', 'performance', 'stage', 'film'],
    'Travelling': ['travel', 'travelling', 'tourism', 'explore', 'adventure'],
    'Gardening': ['garden', 'gardening', 'plants', 'horticulture', 'landscaping'],
    'Animals': ['animals', 'pets', 'wildlife', 'veterinary', 'zoology'],
    'Photography': ['photo', 'photography', 'camera', 'pictures', 'visual'],
    'Teaching': ['teach', 'teaching', 'education', 'tutor', 'instruction'],
    'Exercise': ['exercise', 'workout', 'fitness', 'gym', 'training'],
    'Coding': ['code', 'coding', 'programming', 'software', 'development'],
    'Electricity_Components': ['electrical', 'electronics', 'circuits', 'wiring'],
    'Mechanic_Parts': ['mechanical', 'engineering', 'machines', 'repair'],
    'Computer_Parts': ['computer', 'hardware', 'technology', 'IT', 'tech'],
    'Researching': ['research', 'investigation', 'analysis', 'study'],
    'Architecture': ['architecture', 'building', 'design', 'construction'],
    'Historic_Collection': ['history', 'historical', 'museum', 'artifacts'],
    'Botany': ['botany', 'plants', 'biology', 'nature'],
    'Zoology': ['zoology', 'animals', 'biology', 'wildlife'],
    'Physics': ['physics', 'science', 'quantum', 'mechanics'],
    'Accounting': ['accounting', 'finance', 'bookkeeping', 'numbers'],
    'Economics': ['economics', 'market', 'finance', 'business'],
    'Sociology': ['sociology', 'society', 'social', 'culture'],
    'Geography': ['geography', 'maps', 'earth', 'environment'],
    'Psychology': ['psychology', 'mental', 'behavior', 'counseling'],
    'History': ['history', 'past', 'historical', 'events'],
    'Science': ['science', 'scientific', 'research', 'experiment'],
    'Bussiness_Education': ['business', 'management', 'entrepreneurship'],
    'Chemistry': ['chemistry', 'chemical', 'laboratory', 'reactions'],
    'Mathematics': ['math', 'mathematics', 'numbers', 'calculations'],
    'Biology': ['biology', 'life', 'organisms', 'medical'],
    'Makeup': ['makeup', 'cosmetics', 'beauty', 'styling'],
    'Designing': ['design', 'creative', 'visual', 'graphics'],
    'Content_Writing': ['writing', 'content', 'copywriting', 'articles'],
    'Crafting': ['craft', 'crafting', 'handmade', 'creative'],
    'Literature': ['literature', 'books', 'novels', 'poetry'],
    'Reading': ['reading', 'books', 'knowledge', 'learning'],
    'Cartooning': ['cartoon', 'animation', 'drawing', 'comics'],
    'Debating': ['debate', 'discussion', 'argument', 'speaking'],
    'Astrology': ['astrology', 'stars', 'horoscope', 'celestial'],
    'Hindi': ['hindi', 'language', 'indian'],
    'French': ['french', 'language', 'foreign'],
    'English': ['english', 'language', 'literature'],
    'Urdu': ['urdu', 'language', 'poetry'],
    'Other_Language': ['language', 'linguistics', 'translation'],
    'Makeup_Artist': ['makeup artist', 'beauty', 'cosmetics'],
    'Mechanic': ['mechanic', 'repair', 'automotive', 'maintenance'],
    'Model': ['modeling', 'fashion', 'runway', 'photography'],
    'Sales': ['sales', 'selling', 'marketing', 'customer'],
    'Doctor': ['doctor', 'medical', 'healthcare', 'medicine'],
    'Pharmacist': ['pharmacy', 'medicine', 'drugs', 'healthcare'],
    'Cycling': ['cycling', 'bicycle', 'biking', 'sports'],
    'Knitting': ['knitting', 'sewing', 'textile', 'crafts'],
    'Director': ['director', 'film', 'movie', 'leadership'],
    'Journalism': ['journalism', 'news', 'reporting', 'media'],
    'Business': ['business', 'commerce', 'trade', 'entrepreneurship'],
    'Listening_Music': ['music', 'listening', 'audio', 'sound']
}

# Course categories for better organization
COURSE_CATEGORIES = {
    'Engineering & Technology': [
        'B.Tech Computer Science Engineering',
        'B.Tech Electrical Engineering',
        'B.Tech Mechanical Engineering'
    ],
    'Business & Management': [
        'BBA- Bachelor of Business Administration',
        'BBS- Bachelor of Business Studies',
        'MBA- Master of Business Administration'
    ],
    'Arts & Design': [
        'BFD- Bachelor of Fashion Designing',
        'BFA- Bachelor of Fine Arts',
        'Graphic Design'
    ],
    'Media & Communication': [
        'BJMC- Bachelor of Journalism and Mass Communication',
        'BEM- Bachelor of Event Management'
    ],
    'Science & Research': [
        'B.Sc Physics',
        'B.Sc Chemistry',
        'B.Sc Biology',
        'B.Sc Mathematics'
    ],
    'Healthcare': [
        'MBBS- Bachelor of Medicine',
        'Pharmacy',
        'Nursing'
    ],
    'Law & Legal Studies': [
        'Integrated Law Course- BA + LL.B',
        'LL.B- Bachelor of Laws'
    ]
}

# Career field mapping
CAREER_FIELDS = {
    'Technology': ['Software Developer', 'Data Scientist', 'Systems Analyst', 'Web Developer'],
    'Business': ['Business Analyst', 'Marketing Executive', 'HR Manager', 'Operations Manager'],
    'Creative': ['Graphic Designer', 'Fashion Designer', 'Content Writer', 'Art Director'],
    'Healthcare': ['Doctor', 'Nurse', 'Pharmacist', 'Medical Researcher'],
    'Education': ['Teacher', 'Professor', 'Training Specialist', 'Educational Consultant'],
    'Media': ['Journalist', 'News Anchor', 'Editor', 'Public Relations Officer'],
    'Legal': ['Lawyer', 'Legal Advisor', 'Judge', 'Public Prosecutor'],
    'Finance': ['Financial Analyst', 'Investment Banker', 'Accountant', 'Auditor']
}
