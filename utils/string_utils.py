"""String utility functions for GigMarket platform."""
import re
from typing import Optional


def sanitize_username(username: str) -> str:
    """Sanitize username by removing special characters.
    
    Args:
        username: Raw username input
        
    Returns:
        Sanitized username with only alphanumeric and underscores
    """
    return re.sub(r'[^a-zA-Z0-9_]', '', username)


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to specified length with suffix.
    
    Args:
        text: Text to truncate
        max_length: Maximum length before truncation
        suffix: Suffix to append when truncated
        
    Returns:
        Truncated text with suffix if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug.
    
    Args:
        text: Text to convert to slug
        
    Returns:
        URL-friendly slug
    """
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def extract_hashtags(text: str) -> list[str]:
    """Extract hashtags from text.
    
    Args:
        text: Text containing hashtags
        
    Returns:
        List of hashtags without # symbol
    """
    return re.findall(r'#(\w+)', text)


def mask_email(email: str) -> str:
    """Mask email address for privacy.
    
    Args:
        email: Email address to mask
        
    Returns:
        Masked email (e.g., jo***@example.com)
    """
    if '@' not in email:
        return email
    
    local, domain = email.split('@', 1)
    if len(local) <= 2:
        masked_local = local[0] + '*'
    else:
        masked_local = local[0] + local[1] + '*' * (len(local) - 2)
    
    return f"{masked_local}@{domain}"
