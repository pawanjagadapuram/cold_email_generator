import re

def clean_webpage_content(text: str) -> str:
    """
    Clean and normalize webpage content by removing HTML tags, URLs,
    special characters, and excessive whitespace.
    
    Args:
        text (str): Raw webpage content
        
    Returns:
        str: Cleaned and normalized text
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    
    # Remove URLs
    text = re.sub(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        '',
        text
    )
    
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()